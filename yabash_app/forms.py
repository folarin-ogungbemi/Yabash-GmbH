from django.forms import ModelForm, TextInput, SelectDateWidget, TimeInput, Select
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
            'no_of_guest': Select(attrs={'class': 'form-control'}),
            'event_date': SelectDateWidget(attrs={'class': 'form-control'}),
            'event_time': TimeInput(attrs={'class': 'form-control'}),
            'event_type': Select(attrs={'class': 'form-control'}),
            'event_info': TextInput(attrs={'class': 'form-control'}),
        }
