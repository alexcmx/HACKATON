from django.db import models
from Project.stock.models import *

class Client(Adress):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)






# Create your models here.
