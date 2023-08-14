from django.views.generic import (CreateView, ListView, DetailView,
                                  DeleteView, UpdateView)
from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.db.models import Q
from django.contrib import messages

from .models import Furniture, Comment
from .forms import FurnitureForm, CommentForm


class AddFurniture(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add furniture """
    template_name = "furniture/add_furniture.html"
    model = Furniture
    form_class = FurnitureForm
    success_url = "/furniture/"
    success_message = "Your post was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddFurniture, self).form_valid(form)


class FurnitureItems(ListView):
    """View all furniture items"""

    template_name = "furniture/furniture_items.html"
    model = Furniture
    context_object_name = "furniture_items"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            furniture_items = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(county__icontains=query) |
                Q(room__icontains=query)
            )
        else:
            furniture_items = self.model.objects.all()
        return furniture_items


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
            comment.furniture_post = furniture_post
            comment.save()
            messages.success(request, 'Your comment has been posted!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "furniture/furniture_detail.html",
            {
                "furniture_post": furniture_post,
                "commented": True,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )


class EditFurniture(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, UpdateView):
    """Edit a furniture post"""
    template_name = 'furniture/edit_furniture.html'
    model = Furniture
    form_class = FurnitureForm
    success_url = '/furniture/'
    success_message = "Your post was updated successfully"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteFurniture(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, DeleteView):
    """Delete an item of furniture """
    template_name = 'furniture/furniture_confirm_delete.html'
    model = Furniture
    form_class = FurnitureForm
    success_url = '/furniture/'
    success_message = "Your post was deleted successfully"

    def test_func(self):
        return self.request.user == self.get_object().user


class MyItems(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ Display all post by particular user """

    template_name = "furniture/my_items.html"
    model = Furniture
    context_object_name = "my_items"

    def get_queryset(self):
        return Furniture.objects.filter(user=self.request.user)

    def test_func(self):
        user = self.request.user
        user_items = self.get_queryset().first().user
        return user == user_items
