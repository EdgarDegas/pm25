import json
from . import errors

def extract_code_city(response):
    """
    Extract code from response message along with the city name of the code.

    response: requests.Response.text  
    return: (code, city_name, )
    """
    response = response.strip('()')

    try:
        # some_s is like:
        # "101130201~xinjiang~克拉玛依~Kelamayi~克拉玛依~Kelamayi~990~834000~KLMY~新疆"
        some_s = json.loads(response)[0].get('ref', '')
    except IndexError:  
        # if IndexError is raised, then the returned list must be empty,
        # which means no code is found in this repsonse for this city
        raise errors.CityCodeNotFound()

    some_s_lst = some_s.split('~')

    if len(some_s_lst[0]) != 9:
        # city code length not 9 is invalid
        # which means no city but some similar locations are found
        raise errors.CityCodeNotFound()
        
    return some_s_lst[0], some_s_lst[2]

def extract_aqi(response):
    if response.startswith('<!DOCTYPE HTML>'):
        raise errors.NoWeatherForCode()
    
    try:
        response = response.split('=')[1]
        aqi = json.loads(response)['aqi_pm25']
    except IndexError:
        raise errors.NoWeatherForCode()
    except KeyError:
        raise errors.AQINotAvailable()

    return aqi