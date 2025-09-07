from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_date']  # Fields to display in booking list

    # Optional: Add search and filters
    search_fields = ['booking_date']
    ordering = ['-booking_date']
