import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()

# Import models from hats_rest, here.
from hats_rest.models import LocationVO

# from hats.api.hats_rest.models import LocationVO

def poll():
    while True:
        print('Hats poller polling for data huh')
        print("does it need single quotes try this")
        try:
            print("Attempting to fetch data from wardrobe-api...")
            response = requests.get("http://wardrobe-api:8000/api/locations")
            print(f"Response Status: {response.status_code}")
            print(f"Response Headers: {response.headers}")

            content = json.loads(response.content)

            if "locations" in content:
                print(f"Found {len(content["locations"])} locations.")

                for location in content["locations"]:
                    LocationVO.objects.update_or_create(
                        import_href=location["href"],
                    )
                    print(f"Processed location: {location["href"]}")
            else:
                print("No 'locations' key found in the response.")
        except Exception as e:
            print(e, file=sys.stderr)
            print(f"An error occurred: {e}", file=sys.stderr)
            print(f"Exception type: {type(e).__name__}", file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
