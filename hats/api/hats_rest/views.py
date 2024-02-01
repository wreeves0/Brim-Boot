from django.shortcuts import render, get_object_or_404
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
        "location",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }

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
    else: # POST
        content = json.loads(request.body)

        try:
            location_id = content["location"]
            location = LocationVO.objects.get(id=location_id)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )

        hat = Hat.objects.create(**content)

        return JsonResponse(
            hat,
            encoder=HatListEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET"])
def api_hat_detail(request, id):
    if request.method == "GET":
        try:
            hat = Hat.objects.get(id=id)
            return JsonResponse(
                hat,
                encoder=HatListEncoder,
                safe=False
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            hat = Hat.objects.get(id=id)
            hat.delete()
            return JsonResponse(
                hat,
                encoder=HatListEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
