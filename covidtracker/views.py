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
    for i in UserProfile.objects.all().exclude(user=request.user):
        coords.append([i.latitude, i.longitude])
    print(coords)
    context = {"key" : settings.GOOGLE_API_KEY,
                "coords" : coords}
    return render(request, "covidtracker/index.html", context)