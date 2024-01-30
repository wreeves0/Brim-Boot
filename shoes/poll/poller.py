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
# from shoes_rest.models import BinVO


# def get_bin():
#     response = requests.get("http://wardrobe:8000/api/bin/")
#     content = json.loads(response.content)
#     for bin in content["bin"]:
#         BinVO.objects.update_or_create(
#             defaults={}

#         )


def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            # Write your polling logic, here
            pass
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
