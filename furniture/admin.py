from django.contrib import admin
from .models import Furniture, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Furniture)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
