from django.urls import path, include
from .views import ProductList, ProductDetail, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)