# Generated by Django 3.2.7 on 2021-12-11 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0018_auto_20211211_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_office_location',
            name='Terms_and_condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Terms_and_conditionOOL', to='invoiceApp.terms_and_conditions'),
        ),
    ]