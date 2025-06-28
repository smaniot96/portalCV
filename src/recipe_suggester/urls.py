from django.urls import path
from .views.main import suggest_recipe_view

urlpatterns = [
    path('', suggest_recipe_view, name='recipe_suggestion'),
]
