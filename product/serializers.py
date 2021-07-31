from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Product
        # fields = ['id', 'name', 'brand', 'info', 'price']
        # fields = ['id', 'name', 'brand', 'price']
        fields = '__all__'
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'product']