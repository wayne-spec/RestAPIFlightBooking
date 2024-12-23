Airline Booking System API

This project is a simplified Airline Booking System API developed using Django and Django Rest Framework (DRF). It provides functionalities to manage flights and passengers, including CRUD operations.

Features

Models

Flight: Represents a flight in the airline system.

Fields: flight_number, departure, arrival, origin, destination, capacity

Passenger: Represents a passenger in the system.

Fields: first_name, last_name, email, phone_number, flight (ForeignKey to Flight)

API Endpoints

List all flights and passengers.

Retrieve a single flight or passenger by ID.

Create a new flight or passenger.

Update details of a flight or passenger.

Delete a flight or passenger.

Additional Features

Filtering options (e.g., filter passengers by flight).

Pagination for list endpoints.

Installation

Prerequisites

Python 3.9+

Django 4.0+

Django Rest Framework 3.0+

Steps

Clone the repository:


Navigate to the project directory:

cd 

Create a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Access the API in your browser at http://127.0.0.1:8000/.

API Endpoints

Flight Endpoints

Method

Endpoint

Description

GET

/api/flights/

List all flights

GET

/api/flights/{id}/

Retrieve a specific flight

POST

/api/flights/

Create a new flight

PUT

/api/flights/{id}/

Update an existing flight

DELETE

/api/flights/{id}/

Delete a flight

Passenger Endpoints

Method

Endpoint

Description

GET

/api/passengers/

List all passengers

GET

/api/passengers/{id}/

Retrieve a specific passenger

POST

/api/passengers/

Create a new passenger

PUT

/api/passengers/{id}/

Update an existing passenger

DELETE

/api/passengers/{id}/

Delete a passenger

Models

Flight Model

flight_number: CharField (unique)

departure: DateTimeField

arrival: DateTimeField

origin: CharField

destination: CharField

capacity: IntegerField

Passenger Model

first_name: CharField

last_name: CharField

email: EmailField (unique)

phone_number: CharField

flight: ForeignKey (to Flight)

Design Decisions

Database Relationships:

The Passenger model has a ForeignKey relationship to the Flight model, ensuring a many-to-one relationship (multiple passengers per flight).

Serializers:

PassengerSerializer includes nested details about the associated flight for better data representation.

ViewSets:

Used DRF ViewSets for simplicity and consistency in CRUD operations.

Leveraged mixins to reduce boilerplate code.

Filtering and Pagination:

Added filtering capabilities to viewsets to allow filtering passengers by flight.

Configured pagination to improve performance for large datasets.

Future Enhancements

Implement authentication and authorization.(Admin Authorization)

