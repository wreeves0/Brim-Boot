from django.urls import path
from .api_views import api_show_shoe

urlpatterns = [
    path("shoes/", api_show_shoe, name="api_show_shoe")



]
