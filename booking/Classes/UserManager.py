from __future__ import annotations
from django.contrib.auth import authenticate, login as auth_login
import base64
from booking.Classes.Singletone import Singleton
from django.contrib import auth
import django.http


class UserManager(Singleton):

    @staticmethod
    def create_user(params):
        username = params['username']
        password = params['password']
        from django.contrib.auth.models import User
        user = authenticate(username=username, password=password)
        if user is not None:
            return False
        user = User.objects.create_user(username=username, email='', password=password)
        user.save()
        return True

    def authorization(self: 'UserManager', username: str, password: str, request):
        user = auth.authenticate()


    @staticmethod
    def allUsers():
        from django.contrib.auth.models import User
        return User.objects.all()

    @staticmethod
    def didAuth(request):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).decode('utf-8').split(':')
                    print(uname)
                    print(passwd)
                    user = authenticate(username=uname, password=passwd)
                    if user is not None:
                        if user.is_active:
                            auth_login(request, user)
                            return (True, user)
                        else:
                            return (False, None)

        return (False, None)







