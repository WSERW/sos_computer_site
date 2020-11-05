from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('services', views.services, name='services'),
]