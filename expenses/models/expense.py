from django.db import models
from django.conf import settings

from .category import Category
from .recurrence import Recurrence

class Expense(models.Model):
  EXPENSE_TYPES = (
        ('one-time', 'One-Time'),
        ('recurring', 'Recurring'),
    )
  
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  currency = models.CharField(max_length=3, choices=settings.CURRENCIES)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
  subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_expenses', null=True, blank=True)
  expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
  recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, null=True, blank=True)
  description = models.TextField(blank=True, null=True)
  expense_date = models.DateTimeField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
        return f"{self.expense_type}: {self.amount} {self.currency}"