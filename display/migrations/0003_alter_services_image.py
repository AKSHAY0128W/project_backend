# Generated by Django 5.0.1 on 2024-01-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_alter_services_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
