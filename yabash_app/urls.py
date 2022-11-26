from yabash_app import views
from django.urls import path
from yabash_app.views import BookingCreateView, BookingRecords, BookingUpdateView, BookingDeleteView

urlpatterns = [
    path("", views.Testimonials.as_view(), name="homePage"),
    path('booking/', views.BookingCreateView.as_view(), name="bookingPage"),
    path('records/', views.BookingRecords.as_view(), name="bookingRecord"),
    path('update/<record_id>/', views.BookingUpdateView, name="updateBooking"),
    path('delete/<record_id>/', views.BookingDeleteView, name="deleteBooking"),
]
