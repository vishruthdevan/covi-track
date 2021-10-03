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
    category = request.GET.get('category', 'all')
    if category == 'all':
        for i in UserProfile.objects.all():
            if request.user == i.user:
                coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'current'})
            elif i.covidaffected == 'T':
                coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'affected'})
            elif i.covidaffected == 'F' or i.covidaffected == 'R':
                if i.vaccinated == '0':
                    coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'zerodose'})
                if i.vaccinated == '1':
                    coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'onedose'})
                if i.vaccinated == '2':
                    coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'twodoses'})

    elif category == 'user':
        i = UserProfile.objects.get(user=request.user)
        coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'current'})
    
    elif category == 'zerodose':
        for i in UserProfile.objects.filter(vaccinated='0'):
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'zerodose'})
    
    elif category == 'onedose':
        for i in UserProfile.objects.filter(vaccinated='1'):
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'onedose'})

    elif category == 'twodoses':
        for i in UserProfile.objects.filter(vaccinated='2'):
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'twodoses'})

    elif category == 'affected':
        for i in UserProfile.objects.filter(covidaffected='T'):
            coords.append({"lat" : i.latitude, "lng" : i.longitude, 'type' : 'affected'})
    
    centre  = {'lat': UserProfile.objects.get(user=request.user).latitude, 'lng': UserProfile.objects.get(user=request.user).longitude}
    context = {"key" : settings.GOOGLE_API_KEY,
               "coords" : coords,
               "centre" : centre}

    return render(request, "covidtracker/index.html", context)