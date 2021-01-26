from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from users.views import RoleRequiredMixin
from .forms import AddEventForm
from .models import Event, City, Type



class LoggedView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')


# def wrapper(context: dict, request: HttpRequest) -> dict:
#     context['types'] = Type.objects.all()
#
#     context['cities'] = City.objects.all()
#
#     try:
#         context['user_type'] = request.user.profile.get_role()
#     except AttributeError:
#         pass
#     return context


class HomeView(View):
    def get(self, request: HttpRequest):
        context = {
            'events': Event.objects.all()
        }
        return render(request, 'content/home.html', context)

    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city', 'events']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class SearchView(View):
    def get(self, request):
        name = self.request.GET.get('q', '')
        e_type = int(self.request.GET.get('type', '-1'))
        city = int(self.request.GET.get('city', '-1'))

        query = {}
        if name:
            query['name__icontains'] = name
        if e_type != -1:
            query['type__id'] = e_type
        if city != -1:
            query['localization__id'] = city

        return render(request, 'content/search.html', {
            'events': Event.objects.filter(**query),
            'events_count': Event.objects.filter(**query).count()
        })


class TicketOwnedView(ListView):
    def get(self, request: HttpRequest):
        context = {
            'events': Event.objects.all()
        }
        return render(request, 'content/ticketOwned.html', context)

    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class YourEventsView(View):
    def get(self, request: HttpRequest):
        context = {
            'events': Event.objects.all()
        }
        return render(request, 'content/yourEvents.html', context)


    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class EventsToAcceptView(View):
    def get(self, request: HttpRequest):
        return render(request, 'content/eventsToAccept.html')

    def post(self, request: HttpRequest):
        keys = ['name', 'type', 'city']
        kwars = {key: request.POST[key] for key in keys}
        html = "\n".join(f'<p>{k}: \"{v}\"' for k, v in kwars.items())
        return HttpResponse(html)


class eventPreviewView(DetailView):
    model = Event
    template_name = 'content/eventPreview.html'


class buyHowManyView(DetailView):
    model = Event
    template_name = 'content/buyHowMany.html'


class buyWhatView(DetailView):
    model = Event
    template_name = 'content/buyWhat.html'


class transactionView(DetailView):
    model = Event
    template_name = 'content/transaction.html'


class AddEventView(RoleRequiredMixin, FormView):
    role = 'O'
    form_class = AddEventForm
    template_name = 'content/addevent.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: form_class):
        organizer = self.request.user
        event: Event = Event.objects.create(**form.cleaned_data)
        organizer.profile.organizer_role.event_set.add(event)
        return super().form_valid(form)
