"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from stock.views import StockViewSet, PromiseViewSet, TimeWorkViewSet, DroneViewSet, TrackViewSet
from client.views import ClientViewSet, RequestClientViewSet

router = routers.DefaultRouter()
router.register('stock', StockViewSet)
router.register('promise', PromiseViewSet)
router.register('stock', TimeWorkViewSet)
router.register('drone', DroneViewSet)
router.register('client', ClientViewSet)
router.register('requests', RequestClientViewSet)
router.register('track', TrackViewSet)


urlpatterns = [
    path('api-v1/router/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-v1/filters/', include('stock.urls')),
    path('api-v1/filters/', include('client.urls')),
    path('dron-hack/', include('base.urls')),

]
