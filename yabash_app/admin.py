from django.contrib import admin
from .models import Testimonial, Subscription, Booking, Author, Table
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    search_fields = ['name', 'status']


admin.site.register(Author)

admin.site.register(Subscription)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('client', 'event_type', 'event_date', 'event_time')
    list_display = (
        'client',
        'number_of_guest',
        'event_type',
        'event_date',
        'event_time')
    search_fields = ['client', 'event_type']
    list_filter = ('event_type', 'event_date', 'number_of_guest')


@admin.register(Table)
class TableAdmin(SummernoteModelAdmin):
    list_display = (
        'table_ID',
        'capacity')
