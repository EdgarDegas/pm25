from django.db import models
from datetime import date
from django.utils.timezone import now

# AQI model and manager
class AQIManager(models.Manager):
    def create_aqi(self, city_id, query_id, value):
        new_record = self.create(city_id=city_id, query_id=query_id, value=value)
        new_record.city_id = city_id
        new_record.query_id = query_id
        new_record.value = value
        new_record.save()
        return new_record

class AQI(models.Model):
    city_id = models.IntegerField(default=0)
    value = models.IntegerField(null=True)
    query_id = models.IntegerField(default=0)

    objects = AQIManager()


# City model and manager
class CityManager(models.Manager):
    def create_city(self, name):
        city = self.create(name=name)
        city.name = name
        city.save()
        return city

class City(models.Model):
    name = models.CharField(max_length=15)
    
    objects = CityManager()


# Query model and manager
class QueryManager(models.Manager):
    def create_query(self, date):
        query = self.create(date=date)
        query.save()
        return query

class Query(models.Model):
    date = models.DateField(default=now)

    objects = QueryManager()