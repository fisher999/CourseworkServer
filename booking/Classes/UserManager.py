from __future__ import annotations
from django.db import models
from booking.models import User
from booking.Classes.Singletone import Singleton

class UserManager(Singleton):

    def create_user(self: 'UserManager', username:str, password):
        user = User(name=username, password=password)
        user.save()
        print('User with name {} and password {} was created!'.format(user.name, user.password))
        return user

    def remove_user(self, userId: str):
        rows = User.objects.all()
        if rows.count() > 0:
            user = rows[0]
            print('User with id{} and name {} and  password {} was removed'.format(user.id,user.name,user.password))

            for row in rows:
                row.delete()








