# Generated by Django 4.0.4 on 2022-05-09 16:22

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('postCode', models.CharField(max_length=10)),
                ('house_num', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('phone_num', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('clubID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('actor1', models.CharField(blank=True, max_length=100, null=True)),
                ('actor2', models.CharField(blank=True, max_length=100, null=True)),
                ('actor3', models.CharField(blank=True, max_length=100, null=True)),
                ('ageRating', models.IntegerField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('uniqueId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('accountOptions', models.CharField(blank=True, choices=[('is_student', 'Is Student'), ('is_clubRep', 'Is Clubrep'), ('is_cinema_manager', 'Is Cinema Manager'), ('is_accounts_manager', 'Is Accounts Manager')], default=None, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen', models.CharField(blank=True, choices=[('screen1', 'Screen1'), ('screen2', 'Screen2'), ('screen3', 'Screen3'), ('screen4', 'Screen4'), ('screen5', 'Screen5')], max_length=50, null=True)),
                ('tickets', models.IntegerField(default=300, max_length=300)),
                ('ticketPrice', models.IntegerField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.movies')),
            ],
        ),
        migrations.CreateModel(
            name='ClubRep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubRepFirstName', models.CharField(max_length=50)),
                ('clubRepLastName', models.CharField(max_length=50)),
                ('dob', models.DateField(default=datetime.datetime(2020, 12, 31, 0, 0))),
                ('club_rep_email', models.EmailField(max_length=100, null=True)),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UWE.club')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.BigIntegerField()),
                ('Age', models.IntegerField()),
                ('Seats_quantity', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Showing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.screen')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UWE.movies')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
