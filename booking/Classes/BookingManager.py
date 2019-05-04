from booking.models import Booking, Apartments
import json

class BookingManager:
    @staticmethod
    def make_booking(apartmentId,params):

        user = params['users']
        apartment = Apartments.objects.get(id=apartmentId)
        origin_accomodation = params['origin_accomodation']
        end_accomodation = params['end_accomodation']
        amountOfPersons = params['amountOfPersons']
        date = params['date']

        booking = Booking(user=user, apartments=apartment, origin_accomodation=origin_accomodation,
                          end_accomodation=end_accomodation, amountOfPersons=amountOfPersons, date=date)
        booking.save()

        return booking

    @staticmethod
    def get_booking_list(user_id):
        booking_list = Booking.objects.filter(user__id=user_id)
        booking_dict_array = []

        for booking in booking_list:
            booking_dict = {}
            booking_dict['hotelId'] = booking.apartments.hotel.id
            booking_dict['apartmentsId'] = booking.apartments.id
            booking_dict['originAccomodation'] = booking.origin_accomodation
            booking_dict['endAccomodation'] = booking.end_accomodation
            booking_dict['amountOfPersons'] = booking.amountOfPersons
            booking_dict['date'] = booking.date
            booking_dict_array.append(booking_dict)

        jsonObject = json.dumps(booking_dict_array).encode('utf8')

        return jsonObject
