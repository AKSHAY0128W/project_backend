# Generated by Django 5.0.1 on 2024-01-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login_registration', '0003_rename_customuser_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customer',
            new_name='CustomUser',
        ),
    ]
