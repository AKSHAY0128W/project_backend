# Generated by Django 4.2.6 on 2024-03-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicebooking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='servicebooking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='servicebooking',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='servicebooking',
            name='time',
        ),
    ]
