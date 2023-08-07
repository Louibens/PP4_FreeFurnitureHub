from django.urls import path
from .views import (
    Furniture, AddFurniture, FurnitureItems, FurnitureDetail, DeleteFurniture
)


urlpatterns = [
    path("add/", AddFurniture.as_view(), name="add_furniture"),
    path("", FurnitureItems.as_view(), name="furniture_items"),
    path("<slug:pk>/", FurnitureDetail.as_view(), name="furniture_detail"),
    path("delete/<slug:pk>/", DeleteFurniture.as_view(), name="delete_furniture"),
]