from django.shortcuts import render

from . import WeatherData


def index(request):
    context = {
        'city_value_lst': WeatherData.city_value_lst()
    }

    return render(request, 'map/index.html', context=context)