# Generated by Django 3.0 on 2019-12-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0004_auto_20191209_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.DateField(blank=True, default=False, help_text='ate', null=True),
        ),
    ]
