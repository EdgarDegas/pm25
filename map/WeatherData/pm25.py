from . import cities
from . import errors

def aqi_pm25(city):
    try: 
        city_code = cities.code_of_city(city)
        print('code of {}: {}'.format(city, city_code))
        aqi_pm25 = cities.aqi_pm25_of_city(city_code)
    # except errors.CityCodeNotFound:
    #     return None
    # except errors.NoWeatherForCode:
    #     return None
    # except errors.AQINotAvailable:
    #     return None
    except:
        return None

    return aqi_pm25