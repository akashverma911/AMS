from django.urls import path
from .views import VehicleList, BookingList, BookingView, CancelBookingView

urlpatterns = [
    path('vechicle_list/',VehicleList.as_view(),name="VehicleList"),
    path('booking_list/', BookingList.as_view(), name="BookingList"),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('booking/canel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
]
