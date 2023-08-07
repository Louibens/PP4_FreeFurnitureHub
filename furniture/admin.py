from django.contrib import admin
from .models import Furniture, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Furniture)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
    list_display = (
        "title",
        "furniture_type",
        "room",
        "description",
        "county",
        "town",
        "image",
        "condition",
        "posted_date",
    )
    list_filter = ("furniture_type",)
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'furniture_post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'message']