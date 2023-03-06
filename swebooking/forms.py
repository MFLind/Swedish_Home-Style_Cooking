from django.forms import ValidationError
from django import forms
from .models import TableBooking
from .models import max_number_of_persons_per_hours, get_totalt_bookings_at_time

class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.old_booking = 0
        self.is_edit = False

    def clean(self):
        cleaned_data = super().clean()

        booking_datetime = cleaned_data.get("booking_date_time")
        persons = cleaned_data.get("persons")        
        total_persons = get_totalt_bookings_at_time(booking_datetime)

        if self.is_edit:
            total_persons = total_persons - self.old_booking

        if (total_persons+persons) > max_number_of_persons_per_hours:
            raise ValidationError(f'That time is fully booked, only {max_number_of_persons_per_hours-total_persons} free seat at this hour.')

        return cleaned_data

    class Meta:
        model = TableBooking
        fields = ('name', 'telephone_number', 'persons', 'booking_date_time')
        

