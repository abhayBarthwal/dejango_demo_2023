# Generated by Django 4.2.6 on 2023-10-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0003_rename_client_balance_client_payments_client_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_info',
            name='client_food',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client_info',
            name='client_phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
