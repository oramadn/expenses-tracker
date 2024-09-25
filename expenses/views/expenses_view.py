from django.http import HttpResponse

def index(request):
    return HttpResponse('We are at the index of expense')

# Create new expense
# def expense_create(request):
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('expense_list')
#     else:
#         form = ExpenseForm()
#     return render(request, 'expenses/expense_form.html', {'form': form})

# # Update existing expense
# def expense_update(request, pk):
#     expense = get_object_or_404(Expense, pk=pk)
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect('expense_list')
#     else:
#         form = ExpenseForm(instance=expense)
#     return render(request, 'expenses/expense_form.html', {'form': form})

# # Delete expense
# def expense_delete(request, pk):
#     expense = get_object_or_404(Expense, pk=pk)
#     if request.method == 'POST':
#         expense.delete()
#         return redirect('expense_list')
#     return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})