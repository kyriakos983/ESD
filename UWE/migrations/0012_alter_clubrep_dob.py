# Generated by Django 4.0.4 on 2022-05-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0011_screen_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubrep',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
