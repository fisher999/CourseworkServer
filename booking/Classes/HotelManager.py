from booking.models import Hotel, Apartments, Feedback
import json
from django.db.models import Min, Avg
#from django.db.models import Aggregate


class HotelManager:
    @staticmethod
    def getHotelsJson():
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

        jsonObject = json.dumps(hotelDictArray).encode('utf8')

        return jsonObject

    @staticmethod
    def getHotelsJsonAtPage(page):
        json = HotelManager.getHotelsJson()
        pages = json.count / 5
        newJson = []
        if page < pages:
            for i in range(page*5, (page+1) * 5):
                newJson.append(json[i])
        return newJson