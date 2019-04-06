from django.shortcuts import render
from rest_framework import viewsets
from stock.models import TimeWork, Promise, Stock, Drone
from stock.serializers import StockSerializer, PromiseSerializer, DroneSerializer, TimeWorkSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PromiseViewSet(viewsets.ModelViewSet):
    queryset = Promise.objects.all()
    serializer_class = StockSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class TimeWorkViewSet(viewsets.ModelViewSet):
    queryset = TimeWork.objects.all()
    serializer_class = TimeWorkSerializer


# Create your views here.
