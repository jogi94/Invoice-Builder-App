# Generated by Django 3.1.7 on 2021-11-19 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0007_auto_20211118_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_details',
            name='title',
        ),
    ]
