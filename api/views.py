from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def weather(request):
    return JsonResponse({'message': 'Hello, Weather API!'})