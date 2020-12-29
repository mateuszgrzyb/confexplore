from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

# from users.forms import RegistrationForm


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    pass
    # form_class = RegistrationForm
    # success_url = reverse_lazy('home')
    # template_name = 'users/register.html'
    #
    # def form_valid(self, form: RegistrationForm) -> HttpResponseRedirect:
    #     valid = super(RegisterView, self).form_valid(form)
    #     return valid


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('login')


class ResetPasswordView(View):
    pass
