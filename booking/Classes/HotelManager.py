from booking.models import Hotel, Apartments, Feedback
import json
from django.db.models import Min, Avg
#from django.db.models import Aggregate


class HotelManager:
    @staticmethod
    def getHotels():
        hotels = Hotel.objects.all()
        hotelDictArray = []

        for hotel in hotels:
            dict = {}
            dict['id'] = hotel.id
            dict['country'] = hotel.country.country
            dict['city'] = hotel.city.city
            dict['street'] = hotel.street
            dict['house_index'] = hotel.house_index
            dict['name'] = hotel.name
            value = Apartments.objects.filter(hotel__id=hotel.id).aggregate(Min('price'))['price__min']
            dict['price'] = value
            ratingDict = Feedback.objects.filter(hotel__id=hotel.id).aggregate(Avg('rating'))
            dict['rating'] = ratingDict['rating__avg']
            dict['image_url'] = hotel.imageUrl
            dict['apartments_count'] = Apartments.objects.filter(hotel__id=hotel.id).count()
            if hotel.description == 'NULL':
                dict['description'] = None
            else:
                dict['description'] = hotel.description
            hotelDictArray.append(dict)

        return hotelDictArray

    @staticmethod
    def getHotelsJsonAtPage(page):

        hotelDictArray = HotelManager.getHotels()

        hotel_pages = HotelManager.split(hotelDictArray, 5, [])

        jsonObject = json.dumps(hotel_pages[int(page)]).encode('utf8')

        return jsonObject

    @staticmethod
    def split(arr, size, arrs):
        if len(arr) > size:
            new_array = []
            for index in range(0, size):
                new_array.append(arr.pop(0))
            arrs.append(new_array)
            HotelManager.split(arr, size, arrs)
        else:
            arrs.append(arr)
            return arrs

        return arrs
