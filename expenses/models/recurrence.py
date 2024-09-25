from django.db import models

class Recurrence(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('custom', 'Custom'),
    ]

    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    interval_days = models.IntegerField(null=True, blank=True)
    day_of_week = models.CharField(max_length=10, null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True)
    month_of_year = models.IntegerField(null=True, blank=True)
    next_occurrence_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.frequency} recurrence starting on {self.start_date}"