# Generated by Django 4.2.6 on 2024-02-21 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_service_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_booking',
            old_name='message',
            new_name='address',
        ),
    ]