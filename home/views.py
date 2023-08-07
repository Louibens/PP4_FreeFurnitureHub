from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from furniture.models import Furniture

# Create your views here.


class Index(ListView):
    model = Furniture
    queryset = Furniture.objects.order_by('-posted_date')
    template_name = 'home/index.html'
    context_object_name = 'furniture_items'

    def get_queryset(self):
        return self.model.objects.all()[:6]


class HowItWorks(ListView):
    template_name = 'home/how_it_works.html'
    model = Furniture
 
    def get_queryset(self):
        return self.model.objects.all()[:3]
