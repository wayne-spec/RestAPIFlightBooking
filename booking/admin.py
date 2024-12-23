from django.contrib import admin
from .models import Flight, Passenger

# Register your models here.
models=[Flight,Passenger]

for model in models:
    admin.site.register(model)