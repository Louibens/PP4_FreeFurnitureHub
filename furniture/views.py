from django.views.generic import CreateView, ListView, DetailView

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Furniture
from .forms import FurnitureForm, CommentForm


class AddFurniture(LoginRequiredMixin, CreateView):
    """Add furniture """
    template_name = "furniture/add_furniture.html"
    model = Furniture
    form_class = FurnitureForm
    success_url = "/furniture/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddFurniture, self).form_valid(form)


class FurnitureItems(ListView):
    """View all furniture items"""

    template_name = "furniture/furniture_items.html"
    model = Furniture
    context_object_name = "furniture_items"


class FurnitureDetail(DetailView):
    """View a single item of furniture"""

    def get(self, request, pk, *args, **kwargs):
        queryset = Furniture.objects
        furniture_post = get_object_or_404(queryset, pk=pk)
        comments = furniture_post.comments.order_by("-created_on")

        return render(
            request,
            "furniture/furniture_detail.html",
            {
                "furniture_post": furniture_post,
                "comments": comments,
                "comment_form": CommentForm(),
            },
        )
    
    def post(self, request, pk, *args, **kwargs):

        queryset = Furniture.objects
        furniture_post = get_object_or_404(queryset, pk=pk)
        comments = furniture_post.comments.order_by("-created_on")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = furniture_post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "furniture/furniture_detail.html",
            {
                "furniture_post": furniture_post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )