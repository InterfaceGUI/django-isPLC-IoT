# Generated by Django 3.0.2 on 2020-02-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isplcAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='isplc',
            name='userID',
            field=models.IntegerField(default=0),
        ),
    ]
