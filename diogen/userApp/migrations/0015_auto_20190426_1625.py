# Generated by Django 2.2 on 2019-04-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0014_auto_20190426_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personprofile',
            name='adress',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='birth_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='personprofile',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
