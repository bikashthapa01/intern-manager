# Generated by Django 2.2 on 2019-04-13 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190413_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_joining',
            field=models.DateField(default=datetime.date(2019, 4, 13)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_leaving',
            field=models.DateField(default=datetime.date(2019, 4, 13)),
        ),
    ]
