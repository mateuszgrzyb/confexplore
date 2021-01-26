
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Profile
ROLE =( 
    ("U", "Uczestnik"), 
    ("V", "Wolontariusz"), 
    ("O", "Organizator"), 
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    rodzaj_użytkownika = forms.ChoiceField(choices = ROLE)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','rodzaj_użytkownika']

class emailUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ['email']
class usernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    
