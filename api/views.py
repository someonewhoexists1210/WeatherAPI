from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .calls import today, daily, day


# Create your views here.
def weather(request):
    return HttpResponse('Hello, World!')

def today_view(request):
    location = request.GET.get('location')
    data = today(location)
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    return render(request, 'today.html', {'data': data})

def day_view(request):
    location = request.GET.get('location')
    date = request.GET.get('date')
    data = day(location, date)
    if 'errorCode' in data:        
        if 400 <= data['errorCode'] < 500:
            return render(request, 'error.html', {'errorCode': data['errorCode'], 'error': data['message']})
        return render(request, 'error.html', {'errorCode': 500, 'error': 'Server Error'})
        
    return render(request, 'result.html', {'data': data})

def daily_view(request):
    location = request.GET.get('location')
    date1 = request.GET.get('date1')
    data = daily(location, date1)

    return JsonResponse(data)