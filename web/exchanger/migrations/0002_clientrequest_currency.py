# Generated by Django 4.0.4 on 2022-05-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchanger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('currency_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sign', models.CharField(max_length=50)),
                ('uah', models.FloatField()),
                ('countries', models.CharField(max_length=255)),
            ],
        ),
    ]
