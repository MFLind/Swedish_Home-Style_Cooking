from django.contrib import admin
from .models import TableBooking


class TableBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'booking_date_time', 'persons', 'telephone_number']
    list_filter = ['name', 'booking_date_time', 'telephone_number']
    search_fields = ['name', 'booking_date_time', 'telephone_numnber']


admin.site.register(TableBooking, TableBookingAdmin)
