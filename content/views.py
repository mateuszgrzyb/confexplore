from enum import Enum

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View


class LoggedView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')


class HomeView(View):
    def get(self, request: HttpRequest):
        context = {
            'user_type': request.user
        }
        return render(request, 'content/home.html', context)

    def post(self, request: HttpRequest):
        print(request.POST)
        return HttpResponse()


class SearchView(View):
    pass
