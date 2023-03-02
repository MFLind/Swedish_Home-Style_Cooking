from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_persons(value):
    if value > 15:
        raise ValidationError('Booking cant be for more than 15 persons')


def validate_datetime(value):
    if value < timezone.now():
        raise ValidationError('Booking date and time need to be in future')


class TableBooking(models.Model):

    name = models.CharField(max_length=48)
    booking_date_time = models.DateTimeField('Booking time and date')
    persons = models.PositiveIntegerField(validators=[validate_persons])
    telephone_number = models.CharField(max_length=16)
    booking_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, validators=[validate_datetime])
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f' Account {self.user} did a booking for guest {self.name}, {self.persons} Persons '  \
            f' at {self.booking_date_time}'


    def get_absolute_url(self):
        return reverse('swebooking:edit', kwargs={'id: self.id'})

    