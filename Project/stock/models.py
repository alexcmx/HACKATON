from django.db import models


class Adress(models.Model):
    """
    Адрес
    """
    coutnry = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    longtitude = models.FloatField(default=0)
    house = models.CharField(max_length=255)
    lantitude = models.FloatField(default=0)

    class Meta:
        abstract = True


class Restrection(models.Model):
    """
    Габариты
    """
    all_weigth = models.FloatField(default=0)
    one_weigth = models.FloatField(default=0)
    all_value = models.FloatField(default=0)
    sibarate = models.FloatField(default=0)

    class Meta:
        abstract = True


class SnippingType(models.Model):
    """
    тип дрона
    """
    fly_human = models.BooleanField(default=False)

    fly_self = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Stock(Adress, SnippingType):
    """
    Склад
    """
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)


class TimeWork(models.Model):
    """
    Время работы
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    information = models.TextField(blank=True)
    time_start = models.TimeField(blank=True)
    time_end = models.TimeField(blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Promise(Restrection, SnippingType):
    """
    Посылка
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Drone(Adress, SnippingType):
    """
    Дроне
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    energy = models.FloatField(default=100)
    operation_mode = models.IntegerField(default=0)
    stock = models.ForeignKey(
        Stock, null=True, blank=True, on_delete=models.SET_NULL)
    maxEnegry = models.FloatField(default=100)

class Track(models.Model):
    def __str__(self):
        return self.track
    distance = models.FloatField(max_length=255)
    track = models.TextField(default="")
    drone = models.OneToOneField(Drone, on_delete=models.SET_NULL, null=True)
# Create your models here.
