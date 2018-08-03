from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.

class AQI(models.Model):
    city_id = models.IntegerField(default=0)
    value = models.IntegerField(null=True)
    query_id = models.IntegerField(default=0)

class City(models.Model):
    name = models.CharField(max_length=15)

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