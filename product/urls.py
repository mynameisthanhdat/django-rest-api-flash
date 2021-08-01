from django.urls import path, include
from .views import ProductList, ProductDetail, UserList, UserDetail, ProductHighlight
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/highlight/', ProductHighlight.as_view(), name='product-highlight'),
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)