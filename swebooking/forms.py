from django import forms
from .models import TableBooking


class BookingForm(forms.ModelForm):

    class Meta:
        model = TableBooking
        fields = ('name', 'telephone_number', 'persons', 'booking_date_time')
        

