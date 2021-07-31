from django.urls import path
from .views import ProductList, ProductDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)