# Generated by Django 3.2.6 on 2021-11-30 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_rename_phonenumber_staff_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='emails',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='firstnames',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='lastnames',
            new_name='last_name',
        ),
    ]