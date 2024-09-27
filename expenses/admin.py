from django.contrib import admin
from .models.expense import Expense
from .models.category import Category
from .models.recurrence import Recurrence

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name == "category":
          kwargs["queryset"] = Category.objects.filter(parent__isnull=True)
      return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['category'].widget.attrs.update({
            'x-model': 'category',
            '@change': 'category = $event.target.value'
        })
        return form

    class Media:
        js = ('js/expense_form.js',)

admin.site.register([Category, Recurrence])
