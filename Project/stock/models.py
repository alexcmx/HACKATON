from django.db import models


class Adress(models.Model):
    city = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    rotation = models.CharField(max_length=255, blank=True)

    class Meta:
        abstruct = True


class Restrection(models.Model):
    all_weigth = models.FloatField(default=0)
    one_weigth = models.FloatField(default=0)
    all_value = models.FloatField(default=0)
    sibarate = models.FloatField(default=0)

    class Meta:
        abstruct = True


class SnippingType(models.Model):
    drone = models.BooleanField(default=False)
    eth_aircraft = models.BooleanField(default=False)

    class Meta:
        abstruct = True


class TimeWork(models.Model):
    name = models.CharField(max_length=255)
    information = models.TextField(blank=True)
    time_start = models.TimeField(blank=True)
    time_end = models.TimeField(blank=True)


class Stock(Adress, SnippingType):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)


# Create your models here.
