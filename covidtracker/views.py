from covidtrackerccda.settings import TEMPLATES
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, "covidtracker/index.html", {"key" : settings.GOOGLE_API_KEY})