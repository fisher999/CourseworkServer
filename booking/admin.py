from django.contrib import admin
from booking.models import User, UserBookingHistory, Hotel, Booking, Location, Address, Feedback, Apartments, ApartmentType, Conditions

# Register your models here.
admin.site.register(User)
admin.site.register(UserBookingHistory)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Location)
admin.site.register(Address)
admin.site.register(Feedback)
admin.site.register(Apartments)
admin.site.register(ApartmentType)
admin.site.register(Conditions)