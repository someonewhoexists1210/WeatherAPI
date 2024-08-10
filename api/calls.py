import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta


main_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

load_dotenv('../.env')
api_key = os.getenv('API_KEY').upper()

def today(location):
    url = main_url + f'{location}/today?&unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def xrange(location, startDate, days):
    date_obj = datetime.strptime(startDate, '%Y-%m-%d')
    new_date_obj = date_obj + timedelta(days=days-1)
    new_date_str = new_date_obj.strftime('%Y-%m-%d')    
    url = main_url + f'{location}/{startDate}/{new_date_str}?include=days&unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def day(location, date):
    url = main_url + f'{location}/{date}?&unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def next(location, key, number=1):
    url = main_url + f'{location}/next{number}{key}?unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def last(location, key, number=1):
    if key == 'hours':
        number = 24
    url = main_url + f'{location}/last{number}{key}?unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def tty(location, key):
    url = main_url + f'{location}/{key}?&unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

def to_date(location, key):
    url = main_url + f'{location}/{key}?&unitGroup=metric&lang=en&key={api_key}'
    response = requests.get(url)
    if not response.ok:
        return {'errorCode': response.status_code, 'message': response.text.split(':')[-1]}
    return response.json()

