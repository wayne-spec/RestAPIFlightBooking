from django.urls import path
from .views import (LoginView,LogoutView,auth_status,FlightListCreateView,FlightRetrieveUpdateView,PassengerListCreateView, PassengerRetrieveUpdateView,)

urlpatterns = [
    # Authentication endpoints
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("auth-status/", auth_status, name="auth_status"),

    # Flight endpoints
    path("flights/", FlightListCreateView.as_view(), name="flight_list_create"),
    path("flights/<int:pk>/", FlightRetrieveUpdateView.as_view(), name="flight_detail_update"),

    # Passenger endpoints
    path("passengers/", PassengerListCreateView.as_view(), name="passenger_list_create"),
    path("passengers/<int:pk>/", PassengerRetrieveUpdateView.as_view(), name="passenger_detail_update"),
]
