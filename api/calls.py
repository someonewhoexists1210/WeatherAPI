import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta


main_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

load_dotenv('../.env')
api_key = os.getenv('API_KEY').upper()

def today(location):
    url = main_url + f'{location}/today?&unitGroup=metric&key={api_key}'
    response = requests.get(url)
    return response.json()

def daily(location, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    new_date_obj = date_obj + timedelta(days=7)
    new_date_str = new_date_obj.strftime('%Y-%m-%d')    
    url = main_url + f'{location}/{date}/{new_date_str}?include=days&unitGroup=metric&key={api_key}'
    response = requests.get(url)
    return response.json()