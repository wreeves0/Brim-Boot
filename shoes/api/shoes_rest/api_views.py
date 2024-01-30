from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Shoe
from common.json import ModelEncoder

# Create your views here.
class ShoeListEncoder(ModelEncoder):
    model = Shoe
    property = ["manufacturer", "model_name"]


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    property = ["manufacturer",
                "model_name",
                "color",
                "picture_url",
                ]


@require_http_methods({"GET"})
def api_show_shoe(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        print("Error message")
        return JsonResponse(
            {"shoes": shoes} ,
            encoder=ShoeListEncoder,
            safe=False,
        )
