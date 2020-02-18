# Generated by Django 3.0.2 on 2020-02-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='isplc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('isPLC_ID', models.IntegerField(default=0)),
                ('Xcontact', models.TextField()),
                ('Ycontact', models.TextField()),
                ('Mcontact', models.TextField()),
                ('Dcontact', models.TextField()),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'isplcs',
            },
        ),
    ]