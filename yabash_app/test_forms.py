from django.test import TestCase
from .forms import BookingForm, SubscriptionForm


class TestBookingForm(TestCase):
    def test_form_inputs(self):
        guests = BookingForm({number_of_guest: ''})
        self.assertFalse(guests.is_valid())
