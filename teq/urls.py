from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('girls', views.girls, name="girls"),
    path('junior', views.junior, name="junior"),
    path('apply', views.apply, name="apply"),
    path('project', views.project, name="project")
]