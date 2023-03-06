from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime, date, time
from django.db.models import Sum

max_number_of_persons_per_hours = 50
max_number_of_persons_per_booking = 15


def validate_persons(value):
    if value > max_number_of_persons_per_booking:
        raise ValidationError(f'Booking cant be for more than {max_number_of_persons_per_booking} persons')


def get_totalt_bookings_at_time(value):
        value = value.replace(minute=0).replace(second=0).replace(microsecond=0)
        v2 = value.replace(minute=59).replace(second=0).replace(microsecond=0)
        pset = TableBooking.objects.filter(booking_date_time__gte=value, booking_date_time__lte=v2).aggregate(Sum('persons'))
        total_persons = pset['persons__sum']
        if total_persons is None:
            total_persons = 0

        return total_persons


def validate_datetime(value):
    value = value.replace(minute=0).replace(second=0).replace(microsecond=0)

    if value < timezone.now():
        raise ValidationError('Booking date and time need to be in future')

    if value.hour < 17 or value.hour > 23:
        raise ValidationError('Booking is outside opening hours (17:00 - 00:00)')


class TableBooking(models.Model):

    name = models.CharField(max_length=48)
    booking_date_time = models.DateTimeField(validators=[validate_datetime])
    persons = models.PositiveIntegerField(validators=[validate_persons])
    telephone_number = models.CharField(max_length=16)
    booking_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f' Account {self.user} did a booking for guest {self.name}, {self.persons} Persons '  \
            f' at {self.booking_date_time}'


    def get_absolute_url(self):
        return reverse('swebooking:edit', kwargs={'id: self.id'})


    