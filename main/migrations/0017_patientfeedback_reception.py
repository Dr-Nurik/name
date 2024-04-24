# Generated by Django 5.0 on 2024-03-28 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientfeedback',
            name='reception',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='main.reception'),
        ),
    ]