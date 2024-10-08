# Generated by Django 4.2.7 on 2024-05-19 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_remove_tracks_category_tracks_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг трека'),
        ),
    ]
