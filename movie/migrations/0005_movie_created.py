# Generated by Django 3.2.7 on 2021-09-17 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]