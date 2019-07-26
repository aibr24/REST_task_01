from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView
from django.shortcuts import render




class Flights(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class Bookings(ListAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer