from django.urls import path
from stock.views import StockViewSet, PromiseViewSet, TimeWorkViewSet, DroneViewSet, TrackViewSet
from Project.urls import router
from stock.filters import StockList, PromiseList, DroneList, TimeWorkList, TrackList
urlpatterns = [
    path('stocks', StockList.as_view()),
    path('promises', PromiseList.as_view()),
    path('drones', DroneList.as_view()),
    path('time-works', TimeWorkList.as_view()),
    path('tracks', TrackList.as_view()),

]
