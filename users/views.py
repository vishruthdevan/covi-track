from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import UserForm
from .models import UserProfile
# Create your views here.

class Register(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'registration/register.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.get(user=user)
            userprofile.email = request.POST.get('email')
            userprofile.save()
            # login(request, user)
            return redirect("login")
        return render(request, 'registration/register.html', {'form' : form})

