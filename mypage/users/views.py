from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserLoginForm

from .models import Profile


# Create your views here.
@login_required(login_url="login/")
def hello(request):
    return render(request,"users/home.html",context={"user":request.user})

@login_required(login_url="login/")
def redirect_to(request):
    return render(request,"users/clases.html",context={"user":request.user})

class LoginView(LoginView):
    template_name = "users/login.html"
    form_class= UserLoginForm

class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    template_name= "users/signup_form.html"

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        user = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=user, password=password)
        login(self.request, user)
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect("/")
