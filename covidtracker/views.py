from covidtrackerccda.settings import TEMPLATES
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

# Create your views here.
@login_required
def index(request):
    context = {"key" : settings.GOOGLE_API_KEY,
                "users" : UserProfile.objects.all().exclude(user=request.user)}
    return render(request, "covidtracker/index.html", context)