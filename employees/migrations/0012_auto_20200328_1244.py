# Generated by Django 3.0.4 on 2020-03-28 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_remove_customer_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='contracttime',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='timequota',
        ),
    ]
