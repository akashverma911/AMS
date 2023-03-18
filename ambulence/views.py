from django.shortcuts import render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, DeleteView
from .models import Vehicle,Booking
from .forms import AvailabilityForm

class VehicleList(ListView):
  model = Vehicle


class BookingList(ListView):
  model = Booking
  def get_queryset(self, *args, **kwargs):
    if self.request.user.is_staff:
      booking_list = Booking.objects.all()
      return booking_list
    else :
      booking_list = Booking.objects.filter(user=self.request.user)
      return booking_list

class CancelBookingView(DeleteView):
  model = Booking
  success_url = reverse_lazy('BookingList')

class BookingView(FormView):
  form_class = AvailabilityForm
  template_name = 'availability_form.html'

  def form_valid(self, form):
    data = form.cleaned_data
    vehicle_list = Vehicle.objects.filter(vehicle_type=data['vehicle_category'])
    if len(vehicle_list)==0:
      return HttpResponse("Not Available for booking")
    else:
      booking = Booking.objects.create(
          user=self.request.user,
          vehicle=vehicle_list[0],
          book_in=data['book_in']
      )
      booking.save()
      return HttpResponse(booking)

    
    
  
