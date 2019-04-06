from client.models import Client, RequestClient
from client.serializers import ClientSerializer, RequestClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'


class RequestClientList(generics.ListAPIView):
    queryset = RequestClient.objects.all()
    serializer_class = RequestClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
