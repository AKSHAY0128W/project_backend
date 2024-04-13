# Generated by Django 4.2.6 on 2024-04-13 15:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0004_alter_customer_address_and_more'),
        ('course', '0002_course_enrolled_customers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled_customers',
        ),
        migrations.RemoveField(
            model_name='course_booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='course_booking',
            name='name',
        ),
        migrations.AddField(
            model_name='course_booking',
            name='purchased_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course_booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration.customer'),
        ),
        migrations.AlterModelTable(
            name='course_booking',
            table=None,
        ),
    ]
