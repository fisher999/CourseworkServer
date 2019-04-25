from booking.models import Apartments, ApartmentImages
import json

class ApartmentsManager:
    @staticmethod
    def getApartmentsJsonAtHotelId(id):
        apartments = Apartments.objects.filter(hotel__id=id)
        apartmentsDictArr = []
        for apartment in apartments:
            apartmentDict = {}
            apartmentDict['id'] = apartment.id
            apartmentType = apartment.apartmentType
            apartmentTypeDict = {}
            apartmentTypeDict['name'] = apartmentType.name
            apartmentTypeDict['numberOfRooms'] = apartmentType.numberOfRooms
            apartmentDict['apartmentType'] = apartmentTypeDict
            conditionsDict = {}
            conditions = apartment.conditions
            conditionsDict['wifi'] = conditions.wi_fi
            conditionsDict['pool'] = conditions.pool
            conditionsDict['spa'] = conditions.spa
            conditionsDict['allowedPets'] = conditions.allowed_pets
            conditionsDict['conditioner'] = conditions.conditioner
            conditionsDict['restaraunt'] = conditions.restaraunt
            conditionsDict['bar'] = conditions.bar
            conditionsDict['gym'] = conditions.gym
            apartmentDict['conditions'] = conditionsDict
            apartmentDict['price'] = apartment.price
            pictures = ApartmentImages.objects.filter(apartment__id=apartment.id)
            pictureUrls = []
            for picture in pictures:
                pictureUrls.append(picture.image_url)
            apartmentDict['pictures'] = pictureUrls

            apartmentsDictArr.append(apartmentDict)

        jsonObject = json.dumps(apartmentsDictArr).encode('utf8')
        return jsonObject