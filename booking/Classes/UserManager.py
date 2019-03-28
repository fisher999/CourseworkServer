from __future__ import annotations
from django.db import models
from booking.models import User
from booking.Classes.Singletone import Singleton

class UserManager(Singleton):

    def create_user(self: 'UserManager', username: str, password):
        user = User(name=username, password=password)

        allUsers = User.objects.all()

        for user in allUsers:
            if user.name == username:
                return

        user.save()
        string = 'User with name {} and password {} was created!'.format(user.name, user.password)
        return (user, string)

    def remove_user(self, userId: str):
        rows = User.objects.all()
        if rows.count() > 0:
            user = rows[0]
            deleteResult = 'User with id{} and name {} and  password {} was removed'.format(user.id, user.name, user.password)

            for row in rows:
                row.delete()

        return deleteResult

    @staticmethod
    def allUsers():
        return User.objects.all()






