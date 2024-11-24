from django.urls import path
from landingPage import views

urlpatterns = [
    path('', views.explore)
]
