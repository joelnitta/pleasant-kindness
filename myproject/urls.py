from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('health/', views.health_check, name='health_check'),
]
