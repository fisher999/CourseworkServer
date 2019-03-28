from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.register, name='register'),
    url('/mainpage/', views.main_page, name='main_page')
]