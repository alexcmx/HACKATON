from django.db import models
from Project.stock.models import *

class Client(Adress):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)

class RequestClient(Adress):
    progress_type = (
        (1, "Заказ получен"),
        (2, "В пути"),
        (3, "Заказ готов к выдаче"),
        (4, "Ожидает подтверждения"),
        (5, "Заказ доставлен"),
    )

    progress = models.IntegerField(choises=progress_type)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    dron = models.ForeignKey(Drone, on_delete=models.CASCADE)
    deliveryTime = models.DateTimeField()





# Create your models here.
