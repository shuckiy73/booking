# Generated by Django 3.0.8 on 2020-08-03 12:18

from django.db import migrations, models
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.profile_photo_path),
        ),
    ]