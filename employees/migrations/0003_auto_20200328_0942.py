# Generated by Django 3.0.4 on 2020-03-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20200328_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='heads',
            field=models.IntegerField(default=1),
        ),
    ]
