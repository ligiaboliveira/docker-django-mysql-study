from django.urls import path
from . import views

urlpatterns = [
    path('hello_mundo/', views.hello_mundo, name='hello_mundo'),
]