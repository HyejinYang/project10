# Generated by Django 2.2.7 on 2019-11-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_score_avg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
