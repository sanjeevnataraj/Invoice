# Generated by Django 3.2.5 on 2021-08-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0005_alter_invoices_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='reference',
            field=models.CharField(max_length=25),
        ),
    ]
