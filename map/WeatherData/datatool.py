from datetime import date

from . import pm25
from .cities import city_lst
from ..models import AQI, Query, City

def request_from_web(query_id):
    print('Recent query is outdated, fetching new data...')
    
    city_value_lst = []
    
    for city in city_lst:
        try: # try to get city_id, create one if not exists
            city_id = City.objects.get(name=city).id
        except City.DoesNotExist:
            city_id = City.objects.create_city(city).id
        except: continue

        # get aqi_pm25 value
        value = pm25.aqi_pm25(city)
        append_to_city_value_lst(city_value_lst, city, value)

        # create new aqi record and save
        _ = AQI.objects.create_aqi(city_id, query_id, value)

    return city_value_lst


def fetch_from_db(query_id):
    aqi_records = AQI.objects.filter(query_id=query_id)

    city_value_lst = []

    for aqi_record in aqi_records:
        # get city_name and value, append to lst
        city_id, value = aqi_record.city_id, aqi_record.value
        city_name = City.objects.get(id=city_id).name
        append_to_city_value_lst(city_value_lst, city_name, value)

    return city_value_lst


def append_to_city_value_lst(lst, name, value):
    if value is not None:
        lst.append({
            'name' : name,
            'value': value
        })