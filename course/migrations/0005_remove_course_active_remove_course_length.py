# Generated by Django 4.2.6 on 2024-03-05 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_desc_learning_learning_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='active',
        ),
        migrations.RemoveField(
            model_name='course',
            name='length',
        ),
    ]