from django.urls import path
from .views import (
    Furniture, AddFurniture, FurnitureItems
)


urlpatterns = [
    path("add/", AddFurniture.as_view(), name="add_furniture"),
    path("", FurnitureItems.as_view(), name="furniture_items"),
]