from django.shortcuts import render
from django.views import generic
from .models import Headline


class Hero(generic.ListView):
    model = Headline
    queryset = Headline.objects.filter(status=1)
    template_name = 'index.html'
