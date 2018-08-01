import requests
from . import cities
from . import errors

def pm25(city):
    try: 
        city_code = cities.code_of_city(city)
        aqi_pm25 = cities.aqi_pm25_of_city(city_code)
    except errors.CityCodeNotFound:
        return None
    except errors.NoWeatherForCode:
        return None
    except errors.AQINotAvailable:
        return None

    return aqi_pm25