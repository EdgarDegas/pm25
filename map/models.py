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