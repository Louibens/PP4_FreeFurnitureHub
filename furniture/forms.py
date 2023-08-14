from django import forms
from .models import Furniture, Comment


class FurnitureForm(forms.ModelForm):
    """Form to create a furniture post """

    class Meta:
        model = Furniture
        fields = [
            "title",
            "furniture_type",
            "room",
            "description",
            "county",
            "town",
            "image",
            "image_alt",
            "condition",
        ]

        description = forms.CharField()

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Furniture Title",
            "description": "Description",
            "furniture_type": "Furniture Type",
            "room": "Room",
            "image": "Furniture Image",
            "image_alt": "Describe Image",
            "county": "County",
            "town": "Town",
            "condition": "Condition",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
