# buyer/serializers.py
from rest_framework import serializers
from .models import VisitBooking
from seller.models import Property
from django.contrib.auth.models import User


class VisitBookingSerializer(serializers.ModelSerializer):
    buyer_username = serializers.ReadOnlyField(source='buyer.username')
    property_title = serializers.ReadOnlyField(source='property.title')

    class Meta:
        model = VisitBooking
        fields = '__all__'  # or list them explicitly
