# Generated by Django 5.1.7 on 2025-03-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_shelter_latitude_shelter_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='aadhaar_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
