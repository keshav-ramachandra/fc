# Generated by Django 3.2.8 on 2021-10-15 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreemiumUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.CharField(max_length=255, unique=True)),
                ('quota_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField(blank=True, default=datetime.date(2000, 1, 1))),
                ('profile_photo_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
