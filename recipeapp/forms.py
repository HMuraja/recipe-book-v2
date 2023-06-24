from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ShareRecipeForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Recipe
        widgets = {
            'description': SummernoteWidget(),
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'region': forms.Select(),
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
            'featured_image': ('Add an Image:'),
            'excerpt': ('Summary:'),
            'prep_time': ('Preparation Time (min):'),
            'serves': ('Serves:'),
            'description': ('Description:'),
            'ingredients': ('Ingerdients:'),
            'method': ('Method:'),
        }
