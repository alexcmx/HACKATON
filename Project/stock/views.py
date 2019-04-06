from django.shortcuts import render
from rest_framework import viewsets
from stock.models import TimeWork, Promise, Stock, Drone, Track
from stock.serializers import StockSerializer, PromiseSerializer, DroneSerializer, TimeWorkSerializer, TrackSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PromiseViewSet(viewsets.ModelViewSet):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class TimeWorkViewSet(viewsets.ModelViewSet):
    queryset = TimeWork.objects.all()
    serializer_class = TimeWorkSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
# Create your views here.
