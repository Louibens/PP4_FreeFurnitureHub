from django.shortcuts import render
from django.views import generic
from furniture.models import Furniture

# Create your views here.


class Index(generic.ListView):
    model = Furniture
    queryset = Furniture.objects.order_by('-posted_date')
    template_name = 'index.html'
    paginate = 6
