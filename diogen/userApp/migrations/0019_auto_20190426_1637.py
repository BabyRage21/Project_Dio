# Generated by Django 2.2 on 2019-04-26 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0018_auto_20190426_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personprofile',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 26, 11, 37, 9, 924916, tzinfo=utc)),
        ),
    ]
