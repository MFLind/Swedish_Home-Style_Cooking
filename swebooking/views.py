from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BookingForm


def home(request):
    return render(request, 'swebooking/index.html')


def menu(request):
    return render(request, 'swebooking/menu.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/welcome/')
    else:
        form = BookingForm()

    return render(request, 'swebooking/booking.html', {'form': form})

