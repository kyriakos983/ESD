# Generated by Django 4.0.4 on 2022-05-04 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UWE', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='screenshowing',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UWE.movies'),
        ),
        migrations.AddField(
            model_name='clubrep',
            name='club',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UWE.club'),
        ),
    ]
