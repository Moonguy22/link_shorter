# Generated by Django 4.0.1 on 2022-01-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='origin_url',
            field=models.URLField(unique=True),
        ),
    ]
