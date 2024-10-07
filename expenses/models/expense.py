from django.db import models
from django.conf import settings
from django.utils import timezone

from .category import Category

class Expense(models.Model):
  EXPENSE_TYPES = (
        ('one-time', 'One-Time'),
        ('recurring', 'Recurring'),
    )
  
  RECURRING_INTERVAL_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
  
  name = models.CharField(blank=True, null=True, max_length=100)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  currency = models.CharField(max_length=3, choices=settings.CURRENCIES)
  type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
  subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_expenses', null=True, blank=True)
  description = models.TextField(blank=True, null=True)
  recurring_interval = models.CharField(max_length=10, choices=RECURRING_INTERVAL_CHOICES, null=True, blank=True)
  recurring_frequency = models.PositiveIntegerField(null=True, blank=True, help_text="How often the recurrence happens (e.g., every 2 weeks).")
  start_date = models.DateTimeField(default=timezone.now, null=False, blank=False)
  end_date = models.DateTimeField(null=True, blank=True)
  last_occurrence = models.DateField(null=True, blank=True)
  next_occurrence = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
        return f"{self.type}: {self.amount} {self.currency}"