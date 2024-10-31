from django.urls import path
from .views.expenses_view import ExpenseListCreateView, ExpenseDetailView
from .views.categories_view import CategoryListCreateView, CategoryDetailView, get_subcategories

urlpatterns = [
    path('get-subcategories/', get_subcategories, name='get_subcategories'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]