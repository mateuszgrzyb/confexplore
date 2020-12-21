from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View


class LoggedView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')


class HomeView(LoggedView):
    pass


class SearchView(LoggedView):
    pass
