# Generated by Django 3.2.8 on 2021-10-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]