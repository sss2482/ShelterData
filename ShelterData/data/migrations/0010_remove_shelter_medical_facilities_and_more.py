# Generated by Django 4.2.20 on 2025-03-25 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_shelter_check_members_in_shelter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelter',
            name='medical_facilities',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='resources',
        ),
        migrations.AddField(
            model_name='resource_avalability',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resource_avalability',
            name='shelter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.shelter'),
        ),
        migrations.AddField(
            model_name='resource_avalability',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('ltr', 'ltr'), ('item', 'item')], default='item', max_length=50),
        ),
        migrations.AddField(
            model_name='shelter',
            name='resources_available',
            field=models.ManyToManyField(blank=True, through='data.Resource_avalability', to='data.resource'),
        ),
        migrations.AlterField(
            model_name='resource_avalability',
            name='resource',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.resource'),
        ),
        migrations.CreateModel(
            name='Medical_facility_avalability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('ltr', 'ltr'), ('item', 'item')], default='item', max_length=50)),
                ('medical_facility', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.medical_facility')),
                ('shelter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.shelter')),
            ],
        ),
        migrations.AddField(
            model_name='shelter',
            name='medical_facilities_available',
            field=models.ManyToManyField(blank=True, through='data.Medical_facility_avalability', to='data.medical_facility'),
        ),
    ]
