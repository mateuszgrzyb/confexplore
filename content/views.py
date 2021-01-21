from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View


class LoggedView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')


def wrapper(context: dict, request: HttpRequest) -> dict:
    context['types'] = [
        'Typ 1',
        'Typ 2',
        'Typ 3',
        'Typ 4',
        'Typ 5',
        'Typ 6',
    ]

    context['cities'] = [
        'Krakow',
        'Berlin',
        'Moskwa',
        'Pila',
    ]

    try:
        context['user_type'] = request.user.profile.get_role()
    except AttributeError:
        pass
    return context


class HomeView(View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/home.html', wrapper(context, request))

    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city','events']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class SearchView(View):
    pass

class TicketOwnedView( View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/ticketOwned.html', wrapper(context, request))
 
    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)
        


class YourEventsView( View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/yourEvents.html', wrapper(context, request))
 
    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)
        

