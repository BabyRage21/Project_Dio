# Generated by Django 2.2 on 2019-04-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_person_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]