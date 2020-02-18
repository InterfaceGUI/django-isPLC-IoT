# Generated by Django 3.0.2 on 2020-02-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='Name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='control',
            name='control_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Button'), (2, 'Toggle Switches'), (3, 'Text'), (4, 'Gauge(Not done yet.)'), (5, 'Green Lamp'), (6, 'Yellow Lamp'), (7, 'Red Lamp')]),
        ),
    ]