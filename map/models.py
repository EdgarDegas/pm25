from django.db import models

# Create your models here.

class AQI(models.Model):
    value = models.IntegerField(default=0)
    city = models.CharField(max_length=15)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return 
