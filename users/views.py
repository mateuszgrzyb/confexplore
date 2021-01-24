from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

# from users.forms import RegistrationForm

# ---------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView

from .forms import UserRegisterForm


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            if form.cleaned_data.get('rodzaj_użytkownika') == '1':
                # opcja zwykłego użytkownika 
                print(1)
            if form.cleaned_data.get('rodzaj_użytkownika') == '2':
                # opcja wolontriusza  
                print(2)
            if form.cleaned_data.get('rodzaj_użytkownika') == '3':
                # opcja organizatora  
                print(1)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# class RegisterView(CreateView):
#     pass
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


class ManageUsersView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    TemplateView
):
    def test_func(self):
        return self.request.user.role_name == 'A'

    template_name = 'users/manageusers.html'
