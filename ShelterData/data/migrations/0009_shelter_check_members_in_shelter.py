# Generated by Django 4.2.20 on 2025-03-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_shelter_check_members_in_shelter'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='shelter',
            constraint=models.CheckConstraint(check=models.Q(('max_capacity__gte', models.F('members_in_shelter'))), name='check_members_in_shelter'),
        ),
    ]
