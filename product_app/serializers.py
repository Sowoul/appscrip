from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'
    def validate_stock_quantity(self,value : str):
        if not value.isdigit(): raise serializers.ValidationError("quantity needs to be an integer")
        return int(value)
