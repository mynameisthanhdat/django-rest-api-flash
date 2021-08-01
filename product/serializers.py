from django.db.models import fields
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.HyperlinkedModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')
    class Meta:
        model = Product
        # fields = ['id', 'name', 'brand', 'price']
        # fields = '__all__'
        fields = ['url', 'id', 'name', 'brand', 'info', 'price', 'highlight', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    product = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'product']