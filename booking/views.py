from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,serializers
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Flight, Passenger
from .Serializers import FlightSerializer, PassengerSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Disable CSRF check
        return


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)  # Log the user in
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  # Log the user out
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


def auth_status(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({"isAuthenticated": is_authenticated})


# Views for Flight and Passenger

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class FlightRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        flight_id = self.request.data.get('flight')
        if not flight_id:
            raise serializers.ValidationError({"flight": "This field is required."})
        flight = Flight.objects.get(id=flight_id)
        serializer.save(flight=flight)


class PassengerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        flight_id = self.request.data.get('flight')
        if not flight_id:
            raise serializers.ValidationError({"flight": "This field is required."})
        flight = Flight.objects.get(id=flight_id)
        serializer.save(flight=flight)
