# Generated by Django 3.2.6 on 2021-12-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211201_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enquiry',
            options={'verbose_name_plural': 'Enquiry'},
        ),
        migrations.AlterModelTable(
            name='enquiry',
            table='contact_us',
        ),
    ]
