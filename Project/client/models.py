from django.db import models
from stock.models import *
from math import *
import random

class Client(Adress):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    def __str__(self):
        return self.login

class RequestClient(Adress):
    key = models.IntegerField(default=0)
    progress_type = (
        (1, "Заказ получен"),
        (2, "В пути"),
        (3, "Заказ готов к выдаче"),
        (4, "Ожидает подтверждения"),
        (5, "Заказ доставлен"),
    )
    def __str__(self):
        return self.client.name + self.promise

    progress = models.IntegerField(choices=progress_type)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    deliveryTime = models.DateTimeField()
    promise = models.ForeignKey(Promise, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key = random.randint(20000, 99999)

        trace = self.trace()

        str_ = ""
        for i in trace[1:-1]:
            str_ += str(i.longtitude) + ' ' + str(i.lantitude) + '\n'
        str_ += str(trace[-1][0]) + " " +str(trace[-1][1])
        super().save(*args, **kwargs)
        drone = Drone.objects.get(id=2)
        t= Track.objects.create(distance=trace[0], track=str_)
        t.request_client = RequestClient.objects.get(pk=self.pk)
        t.save()

    def trace(self):
        StockList = Stock.objects.all()
        arr = []
        departure = None
        for i in StockList:
            arr.append((distance(i.longtitude, i.lantitude, self.longtitude, self.lantitude), i))
        arr = sorted(arr, key=lambda x: x[0])
        """arr = [(dist, stock),....]"""
        for i in arr:

            if i[1] == self.promise.stock:
                self.stock = i[1]
                departure = i
        trace_= look4trace((self.longtitude,self.lantitude),departure,arr)
        if trace_==False:
            return [-1, self.stock]
        else:
            return trace_

 # Create your models here.

        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk

# Create your models here.

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def look4trace(client_addr,departure,arr):
    drone=Drone.objects.get(id=2)
    result_arr =[0,departure[1]]
    #резульитат,трак
    if(departure[0]+arr[0][0]<=drone.energy):
        return [departure[0]+arr[0][0],departure[1],client_addr]
    else:
        find = departure
        while True:

            for i in arr:
                if distance(find[1].longtitude,find[1].lantitude,i[1].longtitude,i[1].lantitude)<drone.energy:
                    result_arr[0]+=distance(find[1].longtitude,find[1].lantitude,i[1].longtitude,i[1].lantitude)
                    result_arr.append(i[1])
                    find = i
                    break
                elif find == i:
                    return False

            if find[0] + arr[0][0] < drone.energy:
                result_arr[0] += find[0] + arr[0][0]
                result_arr.append()
                return result_arr
