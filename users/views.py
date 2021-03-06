from django.contrib.auth import logout,login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

# from users.forms import RegistrationForm

# ---------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView

from .forms import UserRegisterForm
from .forms import emailUpdateForm
from .forms import usernameUpdateForm
from .models import Administrator
from .models import NormalUser
from .models import Organizer
from .models import Profile
from .models import Volunteer


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


def register_view(request):

    switch = {
        'V': Volunteer,
        'O': Organizer,
        'U': NormalUser
    }

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            role_name = form.cleaned_data['rodzaj_użytkownika']

            profile = Profile.objects.create(
                django_user=user,
                name=user.username,
                role_name=role_name,
            )

            switch[role_name].objects.create(
                profile=profile
            )

            login(request, user)

            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('login')


class ResetPasswordView(View):
    pass


class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    role = 'A'

    def test_func(self):
        return self.request.user.profile.role_name == self.role


class ManageUsersView(
    #AdminRequiredMixin,
    TemplateView):

    template_name = 'users/manageusers.html'
    extra_context = {
        'profiles': Profile.objects.exclude(role_name='A')
    }


class ConfirmUserView(
    #AdminRequiredMixin,
    View):
    def post(self, request: HttpRequest) -> HttpResponse:
        pk = request.POST["pk"]
        print(request.POST)
        p: Profile = Profile.objects.get(pk=pk)
        r = p.get_role()
        print(f'\n\nCONFIRM USER PK: {pk}')
        r.blocked = not r.blocked
        r.save()
        return redirect('manage_users')

def accountSettingView(request):
    if request.method == 'POST':
        form = usernameUpdateForm(request.POST,request.FILES,instance=request.user.profile) 
        if  form.is_valid():
            form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('home')
    else:
            form = usernameUpdateForm(instance=request.user)
    return render(request, 'users/accountSetting.html',{'form' : form})

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/changePassword.html', {
        'form': form
    })
