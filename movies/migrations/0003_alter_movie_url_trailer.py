# Generated by Django 4.1.7 on 2023-04-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_url_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url_trailer',
            field=models.URLField(max_length=600),
        ),
    ]