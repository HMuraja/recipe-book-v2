from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
