from django.views.generic import CreateView, ListView

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Furniture
from .forms import FurnitureForm


class AddFurniture(LoginRequiredMixin, CreateView):
    """Add furniture """
    template_name = "add_furniture.html"
    model = Furniture
    form_class = FurnitureForm
    success_url = "/furniture/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddFurniture, self).form_valid(form)


class FurnitureItems(ListView):
    """View all furniture items"""

    template_name = "furniture_items.html"
    model = Furniture
    context_object_name = "furniture_items"