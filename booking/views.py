from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from .forms import BookingForm

def booking_view(request):
    min_date = now().date().isoformat()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            messages.success(request, 'Booking confirmed!')
            return redirect('booking:home')
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {
        'form': form,
        'min_date': min_date,
    })
