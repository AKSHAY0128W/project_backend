# Generated by Django 4.2.6 on 2024-02-26 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_course_learning_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learning',
            old_name='desc',
            new_name='learning_description',
        ),
    ]