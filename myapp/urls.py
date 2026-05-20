from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('health/', views.health_check, name='health_check'),
    path('members/', views.members, name='members'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
]
