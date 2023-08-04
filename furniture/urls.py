from django.urls import path
from .views import (
    Furniture, AddFurniture
)


urlpatterns = [
    path("add/", AddFurniture.as_view(), name="add_furniture"),
]