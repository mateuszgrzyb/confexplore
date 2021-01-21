from django.urls import path, re_path

from content.views import HomeView, SearchView,TicketOwnedView,YourEventsView

urlpatterns = [
    path('',        HomeView.as_view(),   name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('ticketOwned/',TicketOwnedView.as_view(),name = 'ticketOwned'),
    path('yourEvents/',YourEventsView.as_view(),name = 'yourEvents')
]
