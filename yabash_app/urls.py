from yabash_app import views
from django.urls import path
from yabash_app.views import Bookings

urlpatterns = [
    path("", views.Testimonials.as_view(), name="homePage"),
    path('booking/', views.Bookings.as_view(), name="bookingPage"),
]
