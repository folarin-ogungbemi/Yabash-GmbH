from yabash_app import views
from django.urls import path

urlpatterns = [
    path('', views.testimonial_and_subscription, name="homePage"),
    path('booking/', views.BookingCreateView.as_view(), name="bookingPage"),
    path('records/', views.BookingRecords.as_view(), name="bookingRecord"),
    path('update/<record_id>/', views.BookingUpdateView, name="updateBooking"),
    path('delete/<record_id>/', views.BookingDeleteView, name="deleteBooking"),
]
