from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
