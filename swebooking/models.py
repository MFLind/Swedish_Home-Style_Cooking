"""
    SweBooking data model
"""
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum

MAX_NUMBER_OF_PERSONS_PER_HOURS = 50
MAX_NUMBER_OF_PERSONS_PER_BOOKING = 15


def validate_persons(value):
    """ Validator for number of persons max in a booking """
    if value > MAX_NUMBER_OF_PERSONS_PER_BOOKING:
        raise ValidationError(f'Booking cant be for more than {MAX_NUMBER_OF_PERSONS_PER_BOOKING} persons')


def get_totalt_bookings_at_time(value):
    """ Helper function to get total number of persons reserved for a day and hour """
    date_start = value.replace(minute=0).replace(second=0).replace(microsecond=0)
    date_end = value.replace(minute=59).replace(second=0).replace(microsecond=0)
    pset = TableBooking.objects.filter(booking_date_time__gte=date_start, booking_date_time__lte=date_end).aggregate(Sum('persons'))
    total_persons = pset['persons__sum']
    if total_persons is None:
        total_persons = 0

    return total_persons


def validate_datetime(value):
    """ Validator for booking that booking date and time isn't in past or outside open hours """
    value = value.replace(minute=0).replace(second=0).replace(microsecond=0)

    if value < timezone.now():
        raise ValidationError('Booking date and time need to be in future')

    if value.hour < 17 or value.hour > 23:
        raise ValidationError('Booking is outside opening hours (17:00 - 00:00)')


class TableBooking(models.Model):
    """
    A class for storing Tablebooking

    """
    name = models.CharField(max_length=48)
    booking_date_time = models.DateTimeField(validators=[validate_datetime])
    persons = models.PositiveIntegerField(validators=[validate_persons])
    telephone_number = models.CharField(max_length=16)
    booking_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """ string print dataset """
        return f' Account {self.user} did a booking for guest {self.name}, {self.persons} Persons '  \
            f' at {self.booking_date_time}'


    def get_absolute_url(self):
        """ get absolute url """
        return reverse('swebooking:edit', kwargs={'id: self.id'})
    