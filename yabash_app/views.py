from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Testimonial
from django.views.generic.edit import FormView
from .forms import BookingForm


class Testimonials(ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1)
    template_name = 'index.html'
    context_object_name = 'testimonials'


class Bookings(FormView):
    template_name = 'booking.html'
    form_class = BookingForm
