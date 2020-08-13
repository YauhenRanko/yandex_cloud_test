import requests
from webapp.config import API_KEY

def api_weather(city_name, date):
    try:
        api_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
        params = {
            "key":API_KEY,
            "q": city_name,
            "format": "json",
            "date": date,
            "lang":"ru"
        }
        result = requests.get(api_url, params=params)
        return result.json()
    except(ConnectionError):
        return False



if __name__ == "__main__":
    weather_test = api_weather('Moscow', 'today')
    print(weather_test)