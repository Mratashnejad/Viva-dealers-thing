# Generated by Django 2.2.10 on 2020-07-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20200708_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Cl', 'Clothes and Uniforms'), ('Ph', 'Phones & Accessories'), ('Je', 'Jewelry & Watches'), ('Ba', 'Bags & Shoes'), ('HA', 'Home Appliance'), ('Be', 'Beauty & Health, Hair'), ('Ap', 'Apartments'), ('Ho', 'Houses')], max_length=2),
        ),
    ]
