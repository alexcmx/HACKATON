from django.db import models
from stock.models import *
from math import *
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

    progress = models.IntegerField(max_length=255, choices=progress_type)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    deliveryTime = models.DateTimeField()
    promise = models.ForeignKey(Promise, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            pass
        super().save(*args, **kwargs)


    def trace(self):
        StockList = Stock.objects.all()
        arr = []
        self.departure = None
        for i in StockList:
            arr.append((distance(self.client.longtitude, self.client.lantitude, self.longtitude, self.lantitude), i))
        arr = sorted(arr, key=lambda x: x[0])
        for i in arr:
            if i[1].promise==self.promise:
                self.departure = i[1].id



        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk





# Create your models here.

def distance(x1,y1,x2,y2):
    return sqrt(abs(x1-x2)+abs(y1-y2))

def look4trace(flong,)