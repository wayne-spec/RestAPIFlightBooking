from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_number','departure','arrival','origin','destination','capacity']

class PassengerSerializer(serializers.ModelSerializer):
    flight_details = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())

    class Meta:
        model = Passenger
        fields = ['first_name','last_name','email','phone_number','flight','flight_details']
