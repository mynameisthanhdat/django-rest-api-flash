from django.urls import path, include
# from .views import ProductList, ProductDetail, UserList, UserDetail, ProductHighlight
from .views import UserViewSet, ProductViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('product/', ProductList.as_view(), name='product-list'),
#     path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
#     path('product/<int:pk>/highlight/', ProductHighlight.as_view(), name='product-highlight'),
#     path('user/', UserList.as_view(), name='user-list'),
#     path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('api-auth/', include('rest_framework.urls')),
# ]

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
product_highlight = ProductViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# urlpatterns = format_suffix_patterns(urlpatterns)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'user', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]