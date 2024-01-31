import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

from shoes_rest.models import BinVO


def get_bins():
    response = requests.get("http://wardrobe-api:8000/api/bins/")
    content = json.loads(response.content)
    for bin in content["bins"]:
        bin_number = bin.get("bin_number")
        closet_name = bin.get("closet_name")
        bin_size = bin.get("bin_size")
        BinVO.objects.update_or_create(
            import_href=bin["href"],
            bin_number=bin_number,
            bin_size=bin_size,
            defaults={"closet_name": closet_name},
        )


def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            get_bins()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
