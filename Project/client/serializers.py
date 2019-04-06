from rest_framework import serializers
from client.models import RequestClient, Client


class RequestClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestClient
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
