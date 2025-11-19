from django.urls import path
from app.views.main import HomePageView

urlpatterns = [
    path("", HomePageView.as_view())
]