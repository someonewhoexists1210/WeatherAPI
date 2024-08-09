from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

load_dotenv('../.env')
api_key = os.getenv('API_KEY').upper()

# Create your views here.
def weather(request):
    # Get the location, date1, and date2 from the request data
    location = request.GET.get('location')
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/today?key={api_key}&include=hours&unitGroup=metric&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&shortColumnNames=false&locationMode=single&utc=false&aggregateHours=24&startDateTime={date1}T00:00:00&endDateTime={date2}T00:00:00'

    response = requests.get(url)

    data = response.json()
    return JsonResponse(data)