from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BookingForm
from .models import TableBooking


def home(request):
    return render(request, 'swebooking/index.html')


def menu(request):
    return render(request, 'swebooking/menu.html')


def seebookings(request):
    tablebookings = TableBooking.objects.filter()
    context = { 'bookings': tablebookings}
    return render(request, 'swebooking/seebookings.html', context)


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/welcome/')
    else:
        form = BookingForm()

    return render(request, 'swebooking/booking.html', {'form': form})

