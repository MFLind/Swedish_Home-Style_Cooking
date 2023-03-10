"""
Swebooking views
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import BookingForm
from .models import TableBooking


APP_NAME = 'swebooking'


def home(request):
    """ index/home page view"""
    return render(request, 'swebooking/index.html')


def menu(request):
    """ menu page view"""
    return render(request, 'swebooking/menu.html')


class SignUpView(generic.CreateView):
    """ Signup page view"""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def seebookings(request):
    """ see bookings/reservations page view"""
    tablebookings = TableBooking.objects.filter().order_by('booking_date_time')
    context = { 'bookings': tablebookings}
    return render(request, 'swebooking/seebookings.html', context)


class BookingView(FormView):
    """ Booking page """
    model = TableBooking
    fields = ['user', 'name', 'telephone_number', 'persons', 'booking_date_time']
    form_class = TableBooking
    template_name = "swebooking/booking.html"
    success_url = 'seebookings'

    def get_form(self):
        """ get form """
        form = BookingForm()

        firstdate = timezone.now().replace(minute=0).replace(second=0).replace(microsecond=0)
        if firstdate.hour < 17:
            firstdate = firstdate.replace(hour=17)
        if firstdate.hour > 23:
            firstdate = firstdate.replace(hour=17).replace(day=firstdate.day+1)

        form.fields['booking_date_time'].initial = firstdate
        form.fields['booking_date_time'].widget = DateTimePickerInput(options={'format': 'YYYY-MM-DD HH:00'})
        return form

    def post(self, request, *args, **kwargs):
        """ post form handler """
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking is added successfully!')
            return redirect('seebookings')

        return render(request, 'swebooking/booking.html', {'form': form})


class EditView(FormView):
    """ Edit booking page """
    model = TableBooking
    fields = ['user', 'name', 'telephone_number', 'persons', 'booking_date_time']
    form_class = TableBooking
    template_name = "swebooking/editbooking.html"
    success_url = 'seebookings'

    def get_form(self):
        """ get form """
        tablebooking = get_object_or_404(TableBooking, id=self.kwargs['booking_id'])
        form = BookingForm(instance=tablebooking)
        form.fields['booking_date_time'].widget = DateTimePickerInput(options={'format': 'YYYY-MM-DD HH:00'})
        return form

    def post(self, request, *args, **kwargs):
        """ post form handler """
        booking = get_object_or_404(TableBooking, id=kwargs['booking_id'])
        form = BookingForm(request.POST)
        form.is_edit = True
        form.old_booking = booking.persons

        if form.is_valid():
            booking.user = request.user
            booking.name = form.cleaned_data['name']
            booking.persons = form.cleaned_data['persons']
            booking.booking_date_time = form.cleaned_data['booking_date_time']
            booking.telephone_number = form.cleaned_data['telephone_number']
            booking.save()
            messages.success(request, 'Your booking is updated successfully!')
            return redirect('seebookings')

        form.fields['booking_date_time'].widget = DateTimePickerInput(options={'format': 'YYYY-MM-DD HH:00'})
        return render(request, 'swebooking/editbooking.html', {'form': form})


class DeleteView(FormView):
    """ Delete ooking page """
    model = TableBooking
    fields = ['user', 'name', 'telephone_number', 'persons', 'booking_date_time']
    form_class = TableBooking
    template_name = "swebooking/delbooking.html"
    success_url = 'seebookings'

    def get_form(self):
        """ get form """
        tablebooking = get_object_or_404(TableBooking, id=self.kwargs['booking_id'])
        form = BookingForm(instance=tablebooking)
        form.fields['booking_date_time'].widget = DateTimePickerInput()
        form.fields['name'].widget.attrs['readonly'] = True
        form.fields['telephone_number'].widget.attrs['readonly'] = True
        form.fields['persons'].widget.attrs['readonly'] = True
        form.fields['booking_date_time'].widget.attrs['readonly'] = True
        return form

    def post(self, request, *args, **kwargs):
        """ post form handler """
        tablebooking = get_object_or_404(TableBooking, id=kwargs['booking_id'])
        if tablebooking.delete():
            messages.success(request, 'Your booking is deleted successfully!')
            return redirect('seebookings')

        return redirect('seebookings')
