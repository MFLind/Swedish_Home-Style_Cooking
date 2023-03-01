from django import forms
from .models import TableBooking
from tempus_dominus.widgets import DateTimePicker
from django.forms.widgets import NumberInput  


class BookingForm(forms.ModelForm):

    class Meta:
        model = TableBooking
        fields = ('name', 'telephone_number', 'persons', 'booking_date_time')

