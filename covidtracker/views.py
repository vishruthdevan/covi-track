from covidtrackerccda.settings import TEMPLATES
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "covidtracker/index.html", {})