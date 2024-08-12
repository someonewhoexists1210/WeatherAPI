from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('get_city/', views.get_city, name='get_city'),
]