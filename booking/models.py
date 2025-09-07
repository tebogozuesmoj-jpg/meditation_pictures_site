from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    booking_hour = models.TimeField(null=True, blank=True)  # Make nullable initially for smooth migration
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)  # Allow nulls initially for migration safety
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        unique_together = ('booking_date', 'booking_hour')  # Prevent double bookings at same slot

    def __str__(self):
        return f"{self.booking_date} at {self.booking_hour} for {self.name or (self.user.username if self.user else 'Guest')}"
