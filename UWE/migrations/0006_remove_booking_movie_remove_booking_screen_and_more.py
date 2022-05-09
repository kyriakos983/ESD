# Generated by Django 4.0.4 on 2022-05-07 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0005_booking_screen_remove_bookingreservation_paid_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='screen',
        ),
        migrations.RemoveField(
            model_name='screen',
            name='movie',
        ),
        migrations.AddField(
            model_name='booking',
            name='showing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.screen'),
        ),
    ]