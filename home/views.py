from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from furniture.models import Furniture

# Create your views here.


class Index(generic.ListView):
    model = Furniture
    queryset = Furniture.objects.order_by('-posted_date')
    template_name = 'home/index.html'
    paginate = 6
    context_object_name = 'furniture_items'

    def get_queryset(self):
        return self.model.objects.all()[:3]
