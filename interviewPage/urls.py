from django.urls import path 
from . import views

urlpatterns = [
    path('', views.interview , name = 'interview'),
]
