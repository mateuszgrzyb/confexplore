from django.urls import path, re_path

from content.views import HomeView, SearchView,TicketOwnedView,YourEventsView,EventsToAcceptView,eventPreviewView, buyHowManyView, buyWhatView, transactionView

urlpatterns = [
    path('',        HomeView.as_view(),   name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('ticketOwned/',TicketOwnedView.as_view(),name = 'ticketOwned'),
    path('yourEvents/',YourEventsView.as_view(),name = 'yourEvents'),
    path('eventsToAccept/',EventsToAcceptView.as_view(),name = 'eventsToAccept'),
    path('eventPreview/',eventPreviewView.as_view(),name = 'eventPreview'),
    path('eventPreview/buyHowMany/', buyHowManyView.as_view(), name='buyHowMany'),
    path('eventPreview/buyHowMany/buyWhat/', buyWhatView.as_view(), name='buyWhat'),
    path('eventPreview/buyHowMany/buyWhat/transaction/', transactionView.as_view(), name='transaction')
]
