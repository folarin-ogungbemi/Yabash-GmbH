from django.contrib import admin
from .models import Testimonial, Author
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ['name', 'status']


admin.site.register(Author)
