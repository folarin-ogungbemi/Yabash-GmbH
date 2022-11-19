from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .models import Testimonial
from .forms import BookingForm


class Testimonials(generic.ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1)
    template_name = 'index.html'
    context_object_name = 'testimonials'


class Bookings(FormView):
    form = BookingForm
    template_name = 'index.html'
    context_object_name = 'bookings'
