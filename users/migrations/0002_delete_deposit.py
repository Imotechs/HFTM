# Generated by Django 4.0.1 on 2022-08-04 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_plan_name_deposit_alter_trade_deposit'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deposit',
        ),
    ]
