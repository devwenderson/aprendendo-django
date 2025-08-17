from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

# Autenticar usuário
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomePageView(TemplateView):
    template_name = "home.html"

class DadosUsuarioView(LoginRequiredMixin, TemplateView):
    template_name = "dados-usuario.html"

class CreateUserView(View):
    template_name = "registration/cadastrar-usuario.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            return redirect("user-create")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect("inicio")

class LoginView(View):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("inicio")
        else:
            return redirect("login")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("inicio")




