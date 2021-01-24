from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from .models import Event, City, Type


class LoggedView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')


def wrapper(context: dict, request: HttpRequest) -> dict:

    context['types'] = Type.objects.all()

    context['cities'] = City.objects.all()

    try:
        context['user_type'] = request.user.profile.get_role()
    except AttributeError:
        pass
    return context


class HomeView(View):
    def get(self, request: HttpRequest):
        context = {
            'events' : Event.objects.all()
        }
        return render(request, 'content/home.html', wrapper(context, request))

    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city','events']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class SearchView(View):
    def get(self, request: HttpRequest):
        query = self.request.GET.get('q')
        loc = 'Warszawa'
        typ = 'Informatyka'
        object_list = Event.objects.filter(
            name__icontains=query
        )

        context = {

        'events' : object_list,
        'loc' : loc,
        'typ' : typ
        }
        return render(request, 'content/search.html', wrapper(context, request))




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
            'events' : Event.objects.all()
        }
        return render(request, 'content/yourEvents.html', wrapper(context, request))
 
    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class EventsToAcceptView( View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/eventsToAccept.html', wrapper(context, request))
 
    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)
        


class eventPreviewView( View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/eventPreview.html', wrapper(context, request))
 
    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)
        

class buyHowManyView (View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/buyHowMany.html', wrapper(context, request))



class buyWhatView (View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/buyWhat.html', wrapper(context, request))


class transactionView (View):
    def get(self, request: HttpRequest):
        context = {
        }
        return render(request, 'content/transaction.html', wrapper(context, request))

