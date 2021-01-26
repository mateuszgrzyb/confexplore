from django.http import HttpRequest

from content.models import City
from content.models import Type


def search(request: HttpRequest) -> dict:
    context = {
        'types': Type.objects.all(),
        'cities': City.objects.all()
    }

    try:
        context['user_type'] = request.user.profile.role_name
    except AttributeError:
        pass

    return context
