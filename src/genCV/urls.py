from django.urls import path
from .views.main import cv_form_view, serve_temp_pdf

urlpatterns = [
    path('', cv_form_view, name='cv_form'),
    path('pdf/<str:filename>/', serve_temp_pdf, name='serve_temp_pdf'),

]
