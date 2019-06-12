from booking.models import Booking, Apartments
import json
from django.utils import timezone
import datetime
import csv
from django.http import HttpResponse

class BookingManager:
    @staticmethod
    def make_booking(params, user):
        apartmentId = params['apartment_id']
        apartment = Apartments.objects.get(id=apartmentId)
        origin_accomodation_string = params['origin_accomodation']
        origin_accomodation = datetime.datetime.strptime(origin_accomodation_string, '%d-%m-%Y')
        end_accomodation_string = params['end_accomodation']
        end_accomodation = datetime.datetime.strptime(end_accomodation_string, '%d-%m-%Y')
        amountOfPersons = params['amount_of_persons']
        date = timezone.now()

        booking = Booking(user=user, apartments=apartment, origin_accomodation=origin_accomodation,
                          end_accomodation=end_accomodation, amountOfPersons=amountOfPersons, date=date)
        booking.save()

        return booking

    @staticmethod
    def get_booking_list(user_id):
        jsonObject = json.dumps(BookingManager.get_booking_dict(user_id)).encode('utf8')

        return jsonObject

    @staticmethod
    def get_booking_dict(user_id):
        booking_list = Booking.objects.filter(user__id=user_id)
        booking_dict_array = []

        for booking in booking_list:
            booking_dict = {}
            booking_dict['id'] = booking.id
            booking_dict['hotel_id'] = booking.apartments.hotel.id
            booking_dict['apartment_id'] = booking.apartments.id
            booking_dict['origin_accomodation'] = booking.origin_accomodation.strftime('%d-%m-%Y')
            booking_dict['end_accomodation'] = booking.end_accomodation.strftime('%d-%m-%Y')
            booking_dict['amount_of_persons'] = booking.amountOfPersons
            booking_dict['date'] = booking.date.strftime('%d-%m-%Y')
            booking_dict_array.append(booking_dict)

        return booking_dict_array

    @staticmethod
    def get_booking_list_csv_response(user_id):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="booking_history.csv"'
        writer = csv.writer(response)
        writer.writerow(['№', 'Название отеля', 'Дата броинирования', 'Дата заезда', 'Дата отъезда', 'Стоимость (руб. в сутки/человек)', 'Число персон', 'Число комнат'])

        booking_list = Booking.objects.filter(user__id=user_id)
        for index, booking in enumerate(booking_list):
            date = booking.date.strftime('%d-%m-%Y')
            origin_accomodation = booking.origin_accomodation.strftime('%d-%m-%Y')
            end_accomodation = booking.end_accomodation.strftime('%d-%m-%Y')
            amount_of_persons = booking.amountOfPersons
            apartment = booking.apartments
            hotel_name = apartment.hotel.name
            price = int(apartment.price) * booking.amountOfPersons
            number_of_rooms = apartment.apartmentType.numberOfRooms
            writer.writerow([index+1, hotel_name, date, origin_accomodation, end_accomodation, price, amount_of_persons, number_of_rooms])

        return response



