from django.urls import path
from .views import (
    Furniture, AddFurniture, FurnitureItems, FurnitureDetail,
    DeleteFurniture, EditFurniture, MyItems
)


urlpatterns = [
    path("add/", AddFurniture.as_view(), name="add_furniture"),
    path("", FurnitureItems.as_view(), name="furniture_items"),
    path("<slug:pk>/", FurnitureDetail.as_view(), name="furniture_detail"),
    path("delete/<slug:pk>/", DeleteFurniture.as_view(),
         name="delete_furniture"),
    path("edit/<slug:pk>/", EditFurniture.as_view(), name="edit_furniture"),
    path("myitems", MyItems.as_view(), name="my_items"),
]
