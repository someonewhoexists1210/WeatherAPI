from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .calls import *


# Create your views here.
def weather(request):
    return today_view(request)

def today_view(request):
    location = request.GET.get('location')
    data = today(location)
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    icon_name = data['currentConditions']['icon']
    return render(request, 'today.html', {'data': data, 'icon': icon_name})

def day_view(request):
    location = request.GET.get('location')
    date = request.GET.get('date')
    data = day(location, date)
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    return render(request, 'day.html', {'data': data})

def range_view(request):
    location = request.GET.get('location')
    date1 = request.GET.get('date1')
    data = xrange(location, date1)

    return render(request, 'daily.html', {'data': data})

def next_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    number = int(request.GET.get('number', 1))
    data = next(location, key, number)
    return dynamic_view(request, data, key)


def last_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    number = int(request.GET.get('number', 1))
    data = last(location, key, number)
    return dynamic_view(request, data, key)


def tty_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    data = tty(location, key)
    return dynamic_view(request, data, key)


def to_date_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    data = to_date(location, key)
    
    return dynamic_view(request, data, key)

def dynamic_view(request, data, key):
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    return render(request, 'daily.html', {'data': data, 'key': key})