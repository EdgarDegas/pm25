import requests
from . import helpers

from . import errors

def code_of_city(city):
    base_url = 'http://toy1.weather.com.cn/search'
    params = { 'cityname': city }
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise errors.WeatherDataNetworkError()

    try:
        code, city_name = helpers.extract_code_city(response.text)
    except errors.CityCodeNotFound:
        raise  # raise this very error
    except:  # while translating other errors into Weather Error
        message = 'Error fetching weather code, inspect traceback for more detail.'
        raise errors.WeatherDataError(message)

    if city != city_name:
        # if city_name of the code is not the same with our city
        # which indicates that no code is available for it
        raise errors.CityCodeNotFound()

    return code

def aqi_pm25_of_city(code):
    url = 'http://d1.weather.com.cn/sk_2d/{}.html'.format(code)
    
    headers = {
        'Referer': 'http://www.weather.com.cn/weather1d/101010100.shtml',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
        }

    response = requests.get(url, headers=headers)

    try:
        aqi_pm25 = helpers.extract_aqi(response.text)
    except errors.AQINotAvailable:
        raise
    except errors.NoWeatherForCode:
        raise
    except:
        message = 'Error fetching AQI_pm25, inspect traceback for more detail.'
        raise errors.WeatherDataError(message)

    return aqi_pm25