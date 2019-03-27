from django.contrib import admin
from booking.models import UserBookingHistory,Hotel,Booking,Location,Address,Feedback,Apartments,ApartmentType,Conditions

# Register your models here.
admin.register(UserBookingHistory)
admin.register(Hotel)
admin.register(Booking)
admin.register(Location)
admin.register(Address)
admin.register(Feedback)
admin.register(Apartments)
admin.register(ApartmentType)
admin.register(Conditions)