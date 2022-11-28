from django import forms
from yabash_app.models import Booking, Subscription


# Create the form class.
class BookingForm(forms.ModelForm):
    event_info = forms.CharField(
        label='Event Information',
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 2,
                'placeholder': "Tell us more about your event...",
                }))

    class Meta:
        model = Booking
        fields = [
            'number_of_guest',
            'event_date',
            'event_time',
            'event_type',
            'event_info']


class SubscriptionForm(forms.ModelForm):
    email = forms.CharField(
        label='Sign up for our Newsletter',
        widget=forms.TextInput(
            attrs={
                'placeholder': "john@example.com",
                }))

    class Meta:
        model = Subscription
        fields = ['email']
