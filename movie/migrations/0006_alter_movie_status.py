# Generated by Django 3.2.7 on 2021-09-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MW', 'MOST WATCHED'), ('MT', 'MOST WATCHED2'), ('TR', 'TOP RATED')], max_length=2),
        ),
    ]
