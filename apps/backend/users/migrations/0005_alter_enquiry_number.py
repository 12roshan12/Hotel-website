# Generated by Django 3.2.6 on 2021-12-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_contactus_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='number',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
