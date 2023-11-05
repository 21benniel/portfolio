from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume_view, name='resume'),
    path('projects/', views.projects_view, name='projects'),
]
