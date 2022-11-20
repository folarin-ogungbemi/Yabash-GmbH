from django.contrib import admin
from .models import Testimonial, Booking, Author, Table
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ['name', 'status']


admin.site.register(Author)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('client', 'event_type', 'event_date', 'event_time')
    list_display = (
        'client',
        'no_of_guest',
        'event_type',
        'event_date',
        'event_time')
    summernote_fields = ('event_info')
    search_fields = ['client', 'event_type']
    list_filter = ('event_type', 'event_date', 'no_of_guest')


@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):
    list_display = (
        'capacity',
        'available',
        'created_on',
        'updated_on')
    list_filter = (
        'capacity',
        'available',)
