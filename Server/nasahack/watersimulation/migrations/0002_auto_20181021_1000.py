# Generated by Django 2.0.7 on 2018-10-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watersimulation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
