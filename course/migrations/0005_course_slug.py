# Generated by Django 5.0.1 on 2024-01-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_resource_alter_course_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
