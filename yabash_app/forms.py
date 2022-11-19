from django.forms import ModelForm, TextInput
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
    widgets = {
            'no_of_guest': TextInput(attrs={'class': 'form-control'}),
            'event_date': TextInput(attrs={'class': 'form-control'}),
            'event_time': TextInput(attrs={'class': 'form-control'}),
            'event_type': TextInput(attrs={'class': 'form-control'}),
            'event_info': TextInput(attrs={'class': 'form-control'}),
        }
