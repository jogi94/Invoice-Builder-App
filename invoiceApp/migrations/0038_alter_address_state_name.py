# Generated by Django 3.2.7 on 2021-12-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0037_address_city_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
