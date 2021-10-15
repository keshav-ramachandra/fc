# Generated by Django 3.2.8 on 2021-10-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('profile_photo_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('forget_pass_code', models.CharField(max_length=100)),
                ('last_login', models.DateField()),
            ],
        ),
    ]
