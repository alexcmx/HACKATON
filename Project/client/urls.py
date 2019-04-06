from client.filters import ClientList, RequestClientList
from Project.urls import router
from django.urls import path
from client.views import RequestClientViewSet, ClientViewSet

urlpatterns = [
    path('clients', ClientList.as_view()),
    path('request', RequestClientList.as_view()),
]
