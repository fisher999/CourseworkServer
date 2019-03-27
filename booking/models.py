from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class UserBookingHistory(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Hotel(models.Model):
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    rating = models.FloatField()

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    originOfAccomodation = models.DateTimeField()
    endOfAccomodation = models.DateTimeField()
    amountOfPersons = models.IntegerField()

class Location(models.Model):
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=50)
    houseIndex = models.CharField(max_length=50)

class Feedback(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=200)

class Apartments(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    apartmentType = models.ForeignKey('ApartmentType', on_delete=models.CASCADE)
    conditions = models.ForeignKey('Conditions', on_delete=models.CASCADE)

class ApartmentType(models.Model):
    name = models.CharField(max_length=50)
    numberOfRooms = models.IntegerField()

class Conditions(models.Model):
    description = models.CharField(max_length=200)







