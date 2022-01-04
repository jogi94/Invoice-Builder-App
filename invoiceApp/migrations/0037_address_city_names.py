# Generated by Django 3.2.7 on 2021-12-13 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0036_city_country_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city_names',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cityA', to='invoiceApp.city'),
        ),
    ]
