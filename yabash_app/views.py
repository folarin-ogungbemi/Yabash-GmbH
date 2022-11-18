from django.shortcuts import render
from django.views import generic
from .models import Testimonial


class Testimonials(generic.ListView):
    model = Testimonial
    queryset = Testimonial.objects.filter(status=1)
    template_name = 'index.html'
