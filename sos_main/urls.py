from django.urls import path, include
<<<<<<< HEAD
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name='sos_main/robots.txt', content_type='text/plain')),
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('services', views.services, name='services'),
=======
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
>>>>>>> 95fb2f6d9db3ba68a3ef6b02c5d212208fb09f7f
]