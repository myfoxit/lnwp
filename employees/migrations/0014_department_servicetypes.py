# Generated by Django 3.0.4 on 2020-03-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_auto_20200328_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='servicetypes',
            field=models.ManyToManyField(to='employees.ServiceType'),
        ),
    ]
