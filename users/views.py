from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .forms import UserForm, InfoForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from django.contrib import messages
from covidtracker.utils import get_ip_address, get_geo
# Create your views here.

class Register(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'registration/register.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.get(user=user)
            userprofile.email = request.POST.get('email')
            userprofile.save()
            username = self.request.POST['username']
            password = self.request.POST['password1']
            #authenticate user then login
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect("users:register_info")
            
        return render(request, 'registration/register.html', {'form' : form})

class Info(View):
    def get(self, request, *args, **kwargs):
        form = InfoForm()
        return render(request, 'registration/register_info.html', {'form': form})

    def post(self, request, *args, **kwargs):
        userprofile = UserProfile.objects.get(user=request.user)
        form = InfoForm(request.POST, instance=userprofile)
        # form.instance.latitude, form.instance.logitude = get_geo(get_ip_address(request))
        if form.is_valid():
            form.save()
            return redirect("covidtracker:index")
        
        return render(request, 'registration/register_info.html', {'form': form})
        

class Profile(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        print(u_form, p_form)
        return render(request, "registration/profile.html", {'u_form': u_form, 'p_form': p_form})

