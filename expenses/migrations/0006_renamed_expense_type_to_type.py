# Generated by Django 5.1.1 on 2024-10-07 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_dropped_recurrences_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='expense_type',
            new_name='type',
        ),
    ]
