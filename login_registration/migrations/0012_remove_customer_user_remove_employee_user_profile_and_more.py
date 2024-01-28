# Generated by Django 5.0.1 on 2024-01-19 10:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0011_rename_first_name_customer_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('customer', 'customer'), ('employee', 'employee')], default='customer', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='login_registration.profile'),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='login_registration.profile'),
        ),
    ]