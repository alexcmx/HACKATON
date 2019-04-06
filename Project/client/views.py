from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from client.models import RequestClient, Client
from client.serializers import RequestClientSerializer, ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RequestClientViewSet(viewsets.ModelViewSet):
    queryset = RequestClient.objects.all()
    serializer_class = RequestClientSerializer

