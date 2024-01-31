from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Shoe, BinVO
from common.json import ModelEncoder

# Create your views here.
class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = ["closet_name", "import_href"]


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = ["manufacturer", "model_name","id"]

    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = ["manufacturer",
                "model_name",
                "color",
                "picture_url",
                "id",
                "bin",

                ]
    encoders = {
        "bin": BinVODetailEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_shoe(request, bin_vo_id=None):
    if request.method == "GET":
        if bin_vo_id is not None:
            shoes = Shoe.objects.filter(bin=bin_vo_id)
        else:
            shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes} ,
            encoder=ShoeListEncoder,
            safe=False,
            )

    else:
        content = json.loads(request.body)
        print(content)

        try:
            if "bin" in content:
                bin_id = content["bin"]
                bin = BinVO.objects.get(id=bin_id)
                content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False
            )




def api_show_shoe(request, pk):

    shoe = Shoe.objects.get(id=pk)
    return JsonResponse(
        shoe,
        encoder=ShoeDetailEncoder,
        safe=False,
    )
