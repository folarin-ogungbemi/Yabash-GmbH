from . import views
from django.urls import path

urlpatterns = [
    path("", views.Hero.as_view(), name="home"),
]