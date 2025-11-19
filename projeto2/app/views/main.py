from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render, redirect

# Models
from app.models import User

# Autenticar
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Forms
from app.forms import UserCreationForm

class HomePageView(TemplateView):
    template_name = "index.html"

class CreateUserView(View):
    template_name = "login/register.html"
    
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("login")
        return redirect("user-create")

class LoginView(View):
    template_name = "login/login.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    # ################## TÁ COM ERRO ##################
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        
        if (user):
            login(request, user)
            return redirect("user-data")
        else:
            return redirect("login")

class LogoutView(View):
    pass

class DataUserView(View, LoginRequiredMixin):
    template_name = "authenticaded_page.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
