from . import views
from django.urls import path

urlpatterns = [
    path("", views.Testimonials.as_view(), name="homePage"),
]
