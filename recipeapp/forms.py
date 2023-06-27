from .models import Comment, Recipe
from django import forms
from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Class for generating comment form.
    """

    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
            'body': ('Leave Comment:'),
            }

        widgets = {
          'body': forms.Textarea(attrs={'rows': 3}),
        }


class ShareRecipeForm(forms.ModelForm):
    """
    Class for generating and editing recipe instances
    """

    class Meta:
        model = Recipe
        widgets = {
            'region': forms.Select(),
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }

        fields = (
            'name',
            'region',
            'city',
            'featured_image',
            'excerpt',
            'prep_time',
            'serves',
            'description',
            'ingredients',
            'method',
            )

        labels = {
            'name': ('Recipe Name:'),
            'region': ('Select the Region:'),
            'city': ('Type the City:'),
            'featured_image': ('Add Image:'),
            'excerpt': ('Summary:'),
            'prep_time': ('Preparation Time (min):'),
            'serves': ('Serves:'),
            'description': ('Description:'),
            'ingredients': ('Ingerdients:'),
            'method': ('Method:'),
        }
