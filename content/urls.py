from django.urls import path, re_path

from content.views import HomeView, SearchView

urlpatterns = [
    path('',        HomeView.as_view(),   name='home'),
    path('search/', SearchView.as_view(), name='search'),
]
