from django.http import HttpResponse
from booking.Classes.UserManager import UserManager


def index(request):
    userManager = UserManager()

    user = userManager.create_user(username='Victor', password='333')
    userManager.remove_user(user.id)

    return HttpResponse("Hello, world. You're at the polls index.")