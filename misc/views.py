from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class FAQView(TemplateView):
    template_name = 'misc/faq.html'


class RegulaminView(TemplateView):
    template_name = 'misc/regulamin.html'


class KontaktView(TemplateView):
    template_name = 'misc/kontakt.html'
