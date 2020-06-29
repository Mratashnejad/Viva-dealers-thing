# Generated by Django 3.0.5 on 2020-06-28 15:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=1, max_length=128, region=None),
            preserve_default=False,
        ),
    ]
