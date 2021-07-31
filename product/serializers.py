from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Product
        # fields = ['id', 'name', 'brand', 'info', 'price']
        # fields = ['id', 'name', 'brand', 'price']
        fields = '__all__'