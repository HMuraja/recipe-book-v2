from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeSelection.as_view(), name='home'),
]
