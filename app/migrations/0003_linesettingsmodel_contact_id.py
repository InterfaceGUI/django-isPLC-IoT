# Generated by Django 3.0.2 on 2020-05-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_linesettingsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='linesettingsmodel',
            name='Contact_ID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
