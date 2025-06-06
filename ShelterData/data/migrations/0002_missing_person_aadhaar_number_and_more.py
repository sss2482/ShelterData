# Generated by Django 5.1.7 on 2025-03-23 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing_person',
            name='aadhaar_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='victim',
            name='shelter_registered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.shelter'),
        ),
    ]
