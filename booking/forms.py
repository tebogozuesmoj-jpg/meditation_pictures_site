from django import forms
from .models import Booking
import datetime

TIME_CHOICES = [
    (datetime.time(hour=10), '10:00 AM'),
    (datetime.time(hour=12), '12:00 PM'),
    (datetime.time(hour=14), '2:00 PM'),
    (datetime.time(hour=16), '4:00 PM'),
]

class BookingForm(forms.ModelForm):
    booking_hour = forms.ChoiceField(choices=TIME_CHOICES, label="Time Slot")

    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_hour', 'name', 'email', 'phone']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'border rounded px-3 py-2'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded px-3 py-2'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded px-3 py-2'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_hour = cleaned_data.get('booking_hour')
        if booking_date and booking_hour:
            existing = Booking.objects.filter(booking_date=booking_date, booking_hour=booking_hour)
            if existing.exists():
                raise forms.ValidationError("This time slot is already booked for the selected date.")
        return cleaned_data
