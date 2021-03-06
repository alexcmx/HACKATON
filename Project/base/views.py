from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "base/index.html"
# Create your views here.

class DronOrderView(TemplateView):
    template_name = "base/dron-order.html"


class DronFindMeView(TemplateView):
    template_name = "base/dron-find-me.html"


class MapView(TemplateView):
    template_name = "base/map.html"