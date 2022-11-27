from django.contrib import admin
from .models import Testimonial, Subscription, Booking, Author, Table, Hour
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
        'capacity',
        'booked_table',
        'table_status',
        'updated_on')
    list_filter = (
        'capacity',
        'booked_table',
        'table_status')


@admin.register(Hour)
class HourAdmin(SummernoteModelAdmin):
    list_display = (
        'hour_ID',
        'hour',
        'booked_hour',
        'hour_status',
        'updated_on'
    )
    list_filter = (
        'hour',
        'booked_hour',
        'hour_status')
