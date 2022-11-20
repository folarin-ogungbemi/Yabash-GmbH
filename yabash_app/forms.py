from django.forms import ModelForm, TextInput, SelectDateWidget, Select
from yabash_app.models import Booking


# Create the form class.
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = [
            'number_of_guest',
            'event_date',
            'event_time',
            'event_type',
            'event_info']
    widgets = {
            'number_of_guest': Select(attrs={'class': 'form-select'}),
            'event_date': SelectDateWidget(attrs={'class': 'form-control'}),
            'event_time': Select(attrs={'class': 'form-select'}),
            'event_type': Select(attrs={'class': 'form-select'}),
            'event_info': TextInput(attrs={'class': 'form-control'}),
        }
