# Generated by Django 4.0.4 on 2022-05-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UWE', '0007_rename_age_booking_age_rename_email_booking_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.movies'),
        ),
        migrations.AddField(
            model_name='screen',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.movies'),
        ),
    ]