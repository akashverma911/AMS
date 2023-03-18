from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
# Create your models here.
class Vehicle(models.Model):
  TYPES = (
      ('Sm', 'Small'),
      ('Md', 'Medium'),
      ('La', 'Large'),
  )
  vehicle_type = models.CharField(max_length=2, choices=TYPES)
  vechicle_no = models.CharField(max_length=50)
  def __str__(self):
    return f'{self.vehicle_type},{self.vechicle_no}'

class Booking(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  book_in = models.DateTimeField()

  def __str__(self):
    return f'{self.user},{self.vehicle},{self.book_in}'

  def get_cancel_booking_url(self):
    return reverse_lazy('CancelBookingView', args=[self.pk,])
