from django import forms


class BookingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=48)
    booking_date_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
        'data-target': '#datetimepicker1'}))
    persons = forms.IntegerField(label='Number of persons', min_value=1)
    telephone_number = forms.CharField(label='Telephone', max_length=16)


