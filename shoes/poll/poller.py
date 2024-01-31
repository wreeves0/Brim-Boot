import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

# Import models from shoes_rest, here.
# from shoes_rest.models import Something
from shoes_rest.models import BinVO


def get_bins():
    response = requests.get("http://wardrobe-api:8000/api/bins/")
    content = json.loads(response.content)
    for bin in content["bins"]:
        bin_number = bin.get("bin_number")  # Extract bin number from the response
        closet_name = bin.get("closet_name")
        bin_size = bin.get("bin_size")  # Extract bin size from the response
        BinVO.objects.update_or_create(
            import_href=bin["href"],
            bin_number=bin_number,
            bin_size=bin_size,  # Use extracted bin size
            defaults={"closet_name": closet_name},  # Use extracted closet name as default
        )




def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            # pass
            # # Write your polling logic, here
            get_bins()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
