from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    pass
