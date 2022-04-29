from multiprocessing import context
from django.shortcuts import render
import requests

from jokes.models import District

# Create your views here.


def index(request):
    return render(request, "index.html")

from django.core.serializers import serialize
import json

def vueapp(request):
    alldistrict = District.objects.all()
    
    alldistrict_json = serialize('json', alldistrict)
    context = {"alldistrict": alldistrict_json}
    return render(request, "vuejs.html", context)
