from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .calls import *
from django.shortcuts import render
from geopy.geocoders import Nominatim


# Create your views here.
def weather(request):
    view = request.GET.get('view')
    if view == 'day':
        return day_view(request)
    if view == 'range':
        return range_view(request)
    if view == 'next':
        return next_view(request)
    if view == 'last':
        return last_view(request)
    if view == 'tty':
        return tty_view(request)
    if view == 'to_date':
        return to_date_view(request)


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
    date1 = request.GET.get('date')
    date2 = request.GET.get('date2')
    data = xrange(location, date1, date2)

    return render(request, 'daily.html', {'data': data})

def next_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    number = int(request.GET.get('number', 1))
    data = next(location, key, number)
    if key == 'hours':
        return render(request, 'hourly.html', {'data': data, key: 'hours'})
    return dynamic_view(request, data, 'next', key)


def last_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    number = int(request.GET.get('number', 1))
    data = last(location, key, number)
    return dynamic_view(request, data, 'last', key)


def tty_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    data = tty(location, key)
    # return JsonResponse(data)
    return render(request, 'tty.html', {'data': data})


def to_date_view(request):
    location = request.GET.get('location')
    key = request.GET.get('key')
    data = to_date(location, key)
    
    return dynamic_view(request, data, 'to_date', key)

def dynamic_view(request, data, view, key):
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    return render(request, 'daily.html', {'data': data, 'view': view, 'key': key})

def get_city_from_coords(lat, lon):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse((lat, lon), exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    if not city:
        city = address.get('town', '') or address.get('village', '')
    return city or "Unknown City"

def get_city(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if lat and lon:
        city = get_city_from_coords(lat, lon)
        return JsonResponse({'city': city})

