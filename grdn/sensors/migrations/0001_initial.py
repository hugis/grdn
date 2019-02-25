# Generated by Django 2.1.7 on 2019-02-25 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='value')),
                ('timestamp', models.DateTimeField(blank=True, help_text='When is observation measured. It is NULL, if sensor has no RTC.', null=True, verbose_name='timestamp')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When is observations stored in database.', verbose_name='created at')),
            ],
            options={
                'verbose_name': 'observation',
                'verbose_name_plural': 'observations',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='meno')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='slug')),
                ('unit', models.CharField(blank=True, choices=[('lux', 'lux'), ('°C', '°C')], max_length=10, verbose_name='unit of data')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'sensor',
                'verbose_name_plural': 'sensors',
            },
        ),
        migrations.AddField(
            model_name='observation',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.Sensor', verbose_name='sensor'),
        ),
    ]
