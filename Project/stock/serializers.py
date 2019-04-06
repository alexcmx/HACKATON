from rest_framework import serializers
from stock.models import TimeWork, Promise, Stock, Drone


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class TimeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWork
        fields = '__all__'


class PromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promise
        fields = '__all__'


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        models = Drone
        fields = '__all__'
