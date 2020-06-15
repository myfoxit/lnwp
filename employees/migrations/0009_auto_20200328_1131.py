# Generated by Django 3.0.4 on 2020-03-28 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_customer_senior'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costcentre',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='costcentre',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='department',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='department',
            name='employee',
        ),
        migrations.AddField(
            model_name='customer',
            name='costcentres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.CostCentre'),
        ),
        migrations.AddField(
            model_name='customer',
            name='departments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='costcentres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.CostCentre'),
        ),
        migrations.AddField(
            model_name='employee',
            name='departments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Department'),
        ),
    ]
