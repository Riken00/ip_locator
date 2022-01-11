from django.shortcuts import render
from django.contrib.gis.utils import GeoIp

# Create your views here.
def home(request):

    if request.method == 'POST' :
        pass

    return render('home.html')