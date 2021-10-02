from covidtrackerccda.settings import TEMPLATES
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

# Create your views here.
@login_required
def index(request):
    coords = list()
    for i in UserProfile.objects.all():
        if request.user == i.user:
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'current'})
        elif i.covidaffected == 'T':
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'affected'})
        elif i.covidaffected == 'F' or i.affected == 'R':
            if i.vaccinated == '0':
                coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'zerodose'})
            if i.vaccinated == '1':
                coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'onedose'})
            if i.vaccinated == '0':
                coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'twodose'})
    
    context = {"key" : settings.GOOGLE_API_KEY,
               "coords" : coords}
    return render(request, "covidtracker/index.html", context)