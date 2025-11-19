from django.urls import path
from app.views.main import HomePageView, CreateUserView, LoginView, DataUserView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("usuario/registrar/", CreateUserView.as_view(), name="user-create"),
    path("usuario/dados/", DataUserView.as_view(), name="user-data"),
    path("login/", LoginView.as_view(), name="login"),
]