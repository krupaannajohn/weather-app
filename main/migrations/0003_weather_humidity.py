# Generated by Django 4.2.5 on 2024-02-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_weather_pressure'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='humidity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]