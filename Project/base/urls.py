from django.urls import path

from base.views import *

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('dron-find-me/',DronFindMeView.as_view(), name='dron-find-me'),
    path('dron-order/', DronOrderView.as_view(), name="dron-order"),
    path('map/', MapView.as_view(), name='map'),

]