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
            'cooking_time',
            'cooking_time',
            'serves',
            'description',
            'ingredients',
            'method',
            )
        
