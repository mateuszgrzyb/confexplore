from django.urls import path, re_path

from content.views import AddEventView
from content.views import EventsToAcceptView
from content.views import HomeView
from content.views import SearchView
from content.views import TicketOwnedView
from content.views import YourEventsView
from content.views import buyHowManyView
from content.views import buyWhatView
from content.views import eventPreviewView
from content.views import transactionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('ticketOwned/', TicketOwnedView.as_view(), name='ticketOwned'),
    path('yourEvents/', YourEventsView.as_view(), name='yourEvents'),
    path('eventsToAccept/', EventsToAcceptView.as_view(), name='eventsToAccept'),
    path('eventPreview/<int:pk>/', eventPreviewView.as_view(), name='eventPreview'),
    path('eventPreview/buyHowMany/', buyHowManyView.as_view(), name='buyHowMany'),
    path('eventPreview/buyHowMany/buyWhat/', buyWhatView.as_view(), name='buyWhat'),
    path('eventPreview/buyHowMany/buyWhat/transaction/', transactionView.as_view(), name='transaction'),
    path('addevent/', AddEventView.as_view(), name='add_event'),
]
