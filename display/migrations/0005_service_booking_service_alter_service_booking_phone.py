# Generated by Django 4.2.6 on 2024-02-21 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_service_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_booking',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='display.services'),
        ),
        migrations.AlterField(
            model_name='service_booking',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]