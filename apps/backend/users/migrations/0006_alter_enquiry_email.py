# Generated by Django 3.2.6 on 2021-12-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_enquiry_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.TextField(),
        ),
    ]
