from django.urls import path
from .api_views import api_list_shoe, api_show_shoe

urlpatterns = [
    path("shoes/", api_list_shoe, name="api_list_shoe"),
    path("shoes/<int:pk>/", api_show_shoe, name="api_show_shoe"),



]
