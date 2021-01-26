from django.forms import ModelForm

from content.models import Event


class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'info', 'localization', 'type', 'date','photo']
