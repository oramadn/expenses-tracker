from django.http import JsonResponse
from django.views.decorators.http import require_GET
from expenses.models import Category
from rest_framework import generics
from ..models.category import Category
from ..serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

@require_GET
def get_subcategories(request):
    try:
        category_id = request.GET.get('category_id')
        if not category_id:
            return JsonResponse({'error': 'Category ID is required'}, status=400)
        
        subcategories = Category.objects.filter(parent_id=category_id).values('id', 'name')
        return JsonResponse(list(subcategories), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)