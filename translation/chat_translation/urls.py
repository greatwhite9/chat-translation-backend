from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_strings, name='process_strings'),  # Route for processing the POST request
]
