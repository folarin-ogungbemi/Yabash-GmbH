from django.contrib import admin
from .models import Testimonial, Headline
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


@admin.register(Headline)
class HeadlineAdmin(SummernoteModelAdmin):
    search_fields = ['headline_text', 'status']
