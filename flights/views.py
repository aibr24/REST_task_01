from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from datetime import date



class Flights(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class Bookings(ListAPIView):
	queryset = Booking.objects.filter(date__gte=date.today())
	serializer_class = BookingSerializer