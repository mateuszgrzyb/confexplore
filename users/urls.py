from django.urls import path

from users.views import LoginView
from users.views import LogoutView
from users.views import ManageUsersView
from users.views import register_view
from users.views import ResetPasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('manage_users/', ManageUsersView.as_view(), name='manage_users'),
]
