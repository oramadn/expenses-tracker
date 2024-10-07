from django.urls import path
from .views import (
    expenses_view,
    categories_view
)

urlpatterns = [
    path('', expenses_view.index, name='expense_list'),
    path('get-subcategories/', categories_view.get_subcategories, name='get_subcategories'),
    # path('create/', expenses_views.expense_create, name='expense_create'),
    # path('<int:pk>/edit/', expenses_views.expense_update, name='expense_update'),
    # path('<int:pk>/delete/', expenses_views.expense_delete, name='expense_delete'),
]