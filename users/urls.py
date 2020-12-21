from django.urls import path

from users.views import LoginView, RegisterView, LogoutView, ResetPasswordView

urlpatterns = [
    path('login/',          LoginView.as_view(),         name='login'),
    path('register/',       RegisterView.as_view(),      name='register'),
    path('logout/',         LogoutView.as_view(),        name='logout'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
]
