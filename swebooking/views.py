from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.urls import reverse_lazy
from django.views import generic
from .forms import BookingForm
from .models import TableBooking

app_name = 'swebooking'

def home(request):
    return render(request, 'swebooking/index.html')


def menu(request):
    return render(request, 'swebooking/menu.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def seebookings(request):
    tablebookings = TableBooking.objects.filter()
    context = { 'bookings': tablebookings}
    return render(request, 'swebooking/seebookings.html', context)


class BookingView(generic.edit.CreateView):
    model = TableBooking
    fields = ['name', 'telephone_number', 'persons', 'booking_date_time']
    template_name = "swebooking/booking.html"

    def get_form(self):
        form = BookingForm()
        form.fields['booking_date_time'].widget = DateTimePickerInput()
        return form


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('seebookings')

    form = BookingForm()
    form.fields['booking_date_time'].widgets = DateTimePickerInput()

    return render(request, 'swebooking/booking.html', {'form': form})


@login_required
def edit(request, id):

    tablebooking = get_object_or_404(TableBooking, id=id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            tablebooking.user = request.user
            tablebooking.persons = form.cleaned_data['persons']
            tablebooking.booking_date_time = form.cleaned_data['booking_date_time']
            tablebooking.telephone_number = form.cleaned_data['telephone_number']
            tablebooking.save()
            return redirect('seebookings')

    form = BookingForm(instance=tablebooking)

    context = { 'booking': tablebooking, 'form': form}

    return render(request, 'swebooking/editbooking.html', context)

@login_required
def delete(request, id):
    tablebooking = get_object_or_404(TableBooking, id=id)

    if request.method == 'POST':
        
        if tablebooking.delete():
            return redirect('seebookings')

    form = BookingForm(instance=tablebooking)

    context = { 'booking': tablebooking, 'form': form}

    return render(request, 'swebooking/delbooking.html', context)
