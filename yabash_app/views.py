from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Testimonial, Booking
from django.views.generic.edit import FormView
from .forms import BookingForm


class Testimonials(ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1)
    template_name = 'index.html'
    context_object_name = 'testimonials'


class BookingRecords(ListView):
    model = Booking
    form_class = BookingForm
    template_name = 'records.html'
    context_object_name = 'records'
    paginate_by = 3

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user.id)


class Bookings(FormView):
    template_name = 'booking.html'
    form_class = BookingForm
