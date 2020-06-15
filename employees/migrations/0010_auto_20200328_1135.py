# Generated by Django 3.0.4 on 2020-03-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20200328_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='costcentres',
        ),
        migrations.AddField(
            model_name='customer',
            name='costcentres',
            field=models.ManyToManyField(to='employees.CostCentre'),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='departments',
        ),
        migrations.AddField(
            model_name='customer',
            name='departments',
            field=models.ManyToManyField(to='employees.Department'),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='costcentres',
        ),
        migrations.AddField(
            model_name='employee',
            name='costcentres',
            field=models.ManyToManyField(to='employees.CostCentre'),
        ),
        migrations.RemoveField(
            model_name='employee',
            name='departments',
        ),
        migrations.AddField(
            model_name='employee',
            name='departments',
            field=models.ManyToManyField(to='employees.Department'),
        ),
    ]
