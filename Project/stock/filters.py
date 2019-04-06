from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from stock.models import TimeWork, Promise, Stock, Drone, Track
from stock.serializers import StockSerializer, PromiseSerializer, DroneSerializer, TimeWorkSerializer, TrackSerializer


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'


class PromiseList(generics.ListAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'


class DroneList(generics.ListAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'


class TimeWorkList(generics.ListAPIView):
    queryset = TimeWork.objects.all()
    serializer_class = TimeWorkSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

class TrackList(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'
