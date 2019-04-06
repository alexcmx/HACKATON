from django.db import models
from Project.stock.models import *

class Client(Adress):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)

class RequestClient(Adress):
    progress = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    dron = models.ForeignKey(Drone, on_delete=models.CASCADE)






# Create your models here.
