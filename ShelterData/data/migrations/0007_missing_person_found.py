# Generated by Django 5.1.7 on 2025-03-23 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_victim_aadhaar_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing_person',
            name='found',
            field=models.BooleanField(default=False),
        ),
    ]
