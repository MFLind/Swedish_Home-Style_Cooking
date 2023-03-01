from django.db import models
from django.contrib.auth.models import User


class TableBooking(models.Model):

    name = models.CharField(max_length=48)
    booking_date_time = models.DateTimeField('Booking time and date')
    persons = models.PositiveIntegerField()
    telephone_number = models.CharField(max_length=16)
    booking_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f' Account {self.user} did a booking for guest {self.name}, {self.persons} Persons '  \
            f' at {self.booking_date_time}'
            