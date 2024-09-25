from django.contrib import admin
from .models.expense import Expense
from .models.category import Category
from .models.recurrence import Recurrence

admin.site.register([Expense, Category, Recurrence])
