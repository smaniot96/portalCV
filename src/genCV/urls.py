from django.urls import path
from .views.main import cv_form_view

urlpatterns = [
    path('', cv_form_view, name='cv_form'),
]
