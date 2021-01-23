# from django.contrib.auth.forms import UserCreationForm
# from users.models import NormalUser
# class RegistrationForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]
#
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

ROLE =( 
    ("1", "Uczestnik"), 
    ("2", "Wolontariusz"), 
    ("3", "Organizator"), 
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    rodzaj_użytkownika = forms.ChoiceField(choices = ROLE)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','rodzaj_użytkownika']
    
