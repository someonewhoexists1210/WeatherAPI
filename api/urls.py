from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
    path('today/', views.today_view, name='today'),
    path('daily/', views.range_view, name='daily'),
    path('day/', views.day_view, name='day'),
    path('next/', views.next_view, name='next'),
    path('last/', views.last_view, name='last'),
    path('tty/', views.tty_view, name='tty'),
    path('to_date/', views.to_date_view, name='to_date'),
]