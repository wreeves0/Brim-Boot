from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse

from common.json import ModelEncoder
from .models import Hat, LocationVO


class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "id",
        "import_href",
        ]

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style_name",
        "color",
        "picture_url",
    ]
    #     "location",
    # ]
    # encoders = {
    #     "location": LocationVODetailEncoder(),
    # }

# Create your views here.

@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatListEncoder,
            safe=False,
        )
