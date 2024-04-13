# Generated by Django 4.2.6 on 2024-04-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0003_employee_package_employee_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Not Specified', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_address',
            field=models.CharField(default='Not Specified', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_email',
            field=models.EmailField(default='Not Specified', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.CharField(default='Not Specified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_phone',
            field=models.CharField(default='Not Specified', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Not Specified', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='Not Specified', max_length=15),
        ),
    ]
