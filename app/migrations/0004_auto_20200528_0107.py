# Generated by Django 3.0.2 on 2020-05-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_linesettingsmodel_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linesettingsmodel',
            name='Contact_Type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Y'), (2, 'M')]),
        ),
    ]