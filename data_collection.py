# data_collection.py

import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = 'a1eb92c311b670fa73879e8650fdc345'
LOCATION = 'Addis Ababa, Ethiopia' 
BASE_URL = 'http://api.openweathermap.org/data/2.5/onecall/timemachine'

def get_weather_data(api_key, location, date):
    params = {
        'lat': location['lat'],
        'lon': location['lon'],
        'dt': int(date.timestamp()),
        'appid': api_key
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def fetch_historical_weather_data(api_key, location, days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    date_generated = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days)]
    
    weather_data = []
    for date in date_generated:
        data = get_weather_data(api_key, location, date)
        weather_data.append(data)
    
    return weather_data

def save_to_csv(weather_data, filename='weather_data.csv'):
    # Convert the data to a pandas DataFrame and save it to a CSV file
    df = pd.DataFrame(weather_data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # Coordinates for Nairobi, Kenya (example)
    location = {'lat': -1.286389, 'lon': 36.817223}
    days = 30  # Number of days to fetch data for
    
    weather_data = fetch_historical_weather_data(API_KEY, location, days)
    save_to_csv(weather_data)
