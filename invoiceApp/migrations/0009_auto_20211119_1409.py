# Generated by Django 3.1.7 on 2021-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceApp', '0008_remove_invoice_details_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='billed_product',
            name='applicable_GST_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='billed_product',
            name='applicable_GST_amount_plus_GST',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, max_length=256, null=True),
        ),
    ]
