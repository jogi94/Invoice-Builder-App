# Generated by Django 3.1.7 on 2021-11-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0009_auto_20211119_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billed_product',
            name='title',
        ),
        migrations.AlterField(
            model_name='billed_product',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='billed_product',
            name='applicable_GST_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='billed_product',
            name='applicable_GST_amount_plus_GST',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=20, max_length=256, null=True),
        ),
    ]
