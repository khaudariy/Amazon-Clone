from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



from .models import Product,Brand,Review,ProductImage
from . import serializers
from .pagination import Mypagination



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle','description']
    ordering_fields = ['name', 'brand','price']


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class = Mypagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['name']
    

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailSerializer    