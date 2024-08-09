from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('today/', views.today_view, name='today'),
    path('daily/', views.daily_view, name='daily'),
]