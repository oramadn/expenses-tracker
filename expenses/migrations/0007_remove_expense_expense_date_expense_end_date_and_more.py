# Generated by Django 5.1.1 on 2024-10-07 18:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_renamed_expense_type_to_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='expense_date',
        ),
        migrations.AddField(
            model_name='expense',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='last_occurrence',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='next_occurrence',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='recurring_frequency',
            field=models.PositiveIntegerField(blank=True, help_text='How often the recurrence happens (e.g., every 2 weeks).', null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='recurring_interval',
            field=models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
