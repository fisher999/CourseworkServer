from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Hotel(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=50, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    house_index = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=50)

    imageUrl = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartments = models.ForeignKey('Apartments', on_delete=models.CASCADE, null=True)
    origin_accomodation = models.DateTimeField()
    end_accomodation = models.DateTimeField()
    amountOfPersons = models.IntegerField()
    date = models.DateTimeField(null=True)


class Country(models.Model):
    country = models.CharField(max_length=30)


class City(models.Model):
    city = models.CharField(max_length=30)


class Feedback(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField()


class Apartments(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    apartmentType = models.ForeignKey('ApartmentType', on_delete=models.CASCADE)
    conditions = models.ForeignKey('Conditions', on_delete=models.CASCADE)
    price = models.FloatField(default=0)


class ApartmentType(models.Model):
    name = models.CharField(max_length=50)
    numberOfRooms = models.IntegerField()


class Conditions(models.Model):
    wi_fi = models.BooleanField(max_length=1, default=False)
    pool = models.BooleanField(max_length=1, default=False)
    spa = models.BooleanField(max_length=1, default=False)
    allowed_pets = models.BooleanField(max_length=1, default=False)
    conditioner = models.BooleanField(max_length=1, default=False)
    restaraunt = models.BooleanField(max_length=1, default=False)
    bar = models.BooleanField(max_length=1, default=False)
    gym = models.BooleanField(max_length=1, default=False)


class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)



