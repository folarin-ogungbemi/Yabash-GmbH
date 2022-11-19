from django.forms import ModelForm
from .models import Booking


# Create the form class.
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = [
            'no_of_guest',
            'event_date',
            'event_time',
            'event_type',
            'event_info']
