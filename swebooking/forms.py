from django import forms
from .models import TableBooking


class BookingForm(forms.ModelForm):

    booking_date_time = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,

                # Calendar and time widget formatting
                'time': 'fa fa-clock-o',
                'date': 'fa fa-calendar',
                'up': 'fa fa-arrow-up',
                'down': 'fa fa-arrow-down',
                'previous': 'fa fa-chevron-left',
                'next': 'fa fa-chevron-right',
                'today': 'fa fa-calendar-check-o',
                'clear': 'fa fa-delete',
                'close': 'fa fa-times'
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )

    class Meta:
        model = TableBooking
        fields = ('name', 'telephone_number', 'persons', 'booking_date_time')
