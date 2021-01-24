from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from users.models import Profile


class FAQView(TemplateView):
    template_name = 'misc/faq.html'
    extra_context = {
        'faq': [{
            'question': f'Question{i}',
            'answer': f'Answer{i}',
        } for i in range(9)]
    }


class RegulaminView(TemplateView):
    template_name = 'misc/regulamin.html'
    extra_context = {
        'regulamin': [{
            'title': f'Title{i}',
            'list': [f'subpoint{j}' for j in range(9)]
        } for i in range(9)]
    }


class KontaktView(TemplateView):
    template_name = 'misc/kontakt.html'
    extra_context = {
        'admins': [{
            'name': f'name{i}',
            'email': f'email{i}',
        } for i in range(9)]
    }
