from . import views
from django.urls import path

urlpatterns = [
    path(
        'edit_recipe/<str:pk>/',
        views.EditRecipe.as_view(),
        name='edit_recipe'),
    path('', views.RecipeSelection.as_view(), name='home'),
    path('recipe_share/', views.ShareRecipe.as_view(), name='recipe_share'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),
]
