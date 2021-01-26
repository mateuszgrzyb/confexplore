from django.contrib.auth import logout,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
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
from .models import Profile


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            request.user.profile.role_name = form.cleaned_data.get('rodzaj_użytkownika')
            request.user.profile.save()            
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# class RegisterView(CreateView):
#     pass
# form_class = RegistrationForm
# success_url = reverse_lazy('home')
# template_name = 'users/register.html'
#
# def form_valid(self, form: RegistrationForm) -> HttpResponseRedirect:
#     valid = super(RegisterView, self).form_valid(form)
#     return valid


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('login')


class ResetPasswordView(View):
    pass


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role_name == 'A'


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
