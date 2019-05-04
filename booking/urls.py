from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^hotels$', views.getHotels, name='hotels'),
    url(r'^hotels/page', views.getHotelsAtPage, name='hotels_at_page'),
    url('/mainpage/', views.main_page, name='main_page'),
    url(r'^hotels/(?P<hotel_id>[0-9]+)/apartments$', views.getApartmentsForId, name='get_apartments_for_id'),
    url(r'^hotels/(?P<hotel_id>[0-9]+)/feedbacks$', views.feedbacksForHotelId, name='feedbacks_for_hotel_id'),
    url(r'^booking/(?P<apartment_id>[0-9]+)$', views.make_booking_for_apartment_id, name='make_booking_for_apartment_id'),
    url(r'^user/booking$', views.get_booking_list, name='get_booking_list')
]