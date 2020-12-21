from django.urls import path

from content.views import HomeView, SearchView

urlpatterns = [
    path('home/',   HomeView.as_view(),   'home'),
    path('search/', SearchView.as_view(), 'search'),
]