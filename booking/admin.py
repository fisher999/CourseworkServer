from django.contrib import admin
from booking.models import Hotel, Booking, City, Country, ApartmentImages, Feedback, Apartments, ApartmentType, \
    Conditions

# Register your models here.
admin.site.register(ApartmentImages)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Country)
admin.site.register(Feedback)
admin.site.register(Apartments)
admin.site.register(ApartmentType)
admin.site.register(Conditions)