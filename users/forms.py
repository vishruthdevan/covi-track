from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")


class InfoForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("contact_number", "address", "town", "state", "post_code", "country", "covidaffected", "vaccinated")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("contact_number", "address", "town", "state", "post_code", "country")


class AuthForm(AuthenticationForm):
    '''
    Form that uses built-in AuthenticationForm to handel user auth
    '''
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
