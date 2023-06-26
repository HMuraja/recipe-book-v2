from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeSelection.as_view(), name='home'),
    path(
        'edit_recipe/<str:pk>/',
        views.EditRecipe.as_view(),
        name='edit_recipe'),

    path(
        'delete_recipe/<str:pk>/',
        views.DeleteRecipe.as_view(),
        name='delete_recipe'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='recipe_like'),
    path('recipe_share/', views.ShareRecipe.as_view(), name='recipe_share'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),
]
