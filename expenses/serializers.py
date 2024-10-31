from rest_framework import serializers
from .models.expense import Expense, Category

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value
      
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')