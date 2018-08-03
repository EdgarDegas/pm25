from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.

class AQI(models.Model):
    city_id = models.IntegerField(default=0)
    value = models.IntegerField(null=True)
    query_id = models.IntegerField(default=0)

    @staticmethod
    def fetch_by_query_id(query_id):
        return AQI.objects.filter(query_id=query_id)


class City(models.Model):
    name = models.CharField(max_length=15)

    @staticmethod
    def fetch_by_id(city_id):
        return City.objects.get(id=city_id)

    @staticmethod
    def fetch_by_name(city_name):
        return City.objects.get(name=city_name)

    @staticmethod
    def create_new_city(name):
        new_city = City()
        new_city.name = name
        new_city.save()
        return new_city.id, new_city


class Query(models.Model):
    date = models.DateField(default=now)

    @staticmethod
    def create_new_query(date):
        new_query = Query()
        new_query.date = date
        new_query.save()
        return new_query.id, new_query

    @staticmethod
    def recent_query():
        return Query.objects.last()