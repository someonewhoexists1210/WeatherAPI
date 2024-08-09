from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .calls import today, daily


# Create your views here.
def weather(request):
    return HttpResponse('Hello, World!')

def today_view(request):
    location = request.GET.get('location')
    data = today(location)
    
    return render(request, 'result.html', {'data': data})

def daily_view(request):
    location = request.GET.get('location')
    date1 = request.GET.get('date1')
    data = daily(location, date1)

    return JsonResponse(data)