# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-16 15:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_delete_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 15, 52, 35, 776643)),
        ),
    ]
