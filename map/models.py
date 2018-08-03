from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.

class AQI(models.Model):
    city_id = models.IntegerField(default=0)
    value = models.IntegerField(null=True)
    query_id = models.IntegerField(default=0)

    @classmethod
    def fetch_by_query_id(cls, query_id):
        return cls.objects.filter(query_id=query_id)

    @classmethod
    def create_new_aqi(cls, city_id, query_id, value):
        new_record = cls()
        new_record.city_id = city_id
        new_record.query_id = query_id
        new_record.value = value
        new_record.save()
        return new_record.id, new_record


class City(models.Model):
    name = models.CharField(max_length=15)

    @classmethod
    def fetch_by_id(cls, city_id):
        return cls.objects.get(id=city_id)

    @classmethod
    def fetch_by_name(cls, city_name):
        return cls.objects.get(name=city_name)

    @classmethod
    def create_new_city(cls, name):
        new_city = cls()
        new_city.name = name
        new_city.save()
        return new_city.id, new_city


class Query(models.Model):
    date = models.DateField(default=now)

    @classmethod
    def create_new_query(cls, date):
        new_query = cls()
        new_query.date = date
        new_query.save()
        return new_query.id, new_query

    @classmethod
    def recent_query(cls):
        return cls.objects.last()