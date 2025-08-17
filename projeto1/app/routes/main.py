from django.urls import path
from app.views.main import HomePageView, DadosUsuarioView, CreateUserView, LoginView, LogoutView

urlpatterns = [
    path("", HomePageView.as_view(), name='inicio'),

    path("usuario/perfil/", DadosUsuarioView.as_view(), name='user-detail'),
    path("usuario/cadastrar/", CreateUserView.as_view(), name='user-create'),

    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),

]