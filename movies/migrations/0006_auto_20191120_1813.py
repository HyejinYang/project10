# Generated by Django 2.2.7 on 2019-11-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_score_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score_sum',
            field=models.IntegerField(default=0),
        ),
    ]