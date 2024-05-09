from rest_framework import serializers
from .models import Product,Brand,Review,ProductImage
from taggit.serializers import (TagListSerializerField,TaggitSerializer)




class ProductImageSerliazer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['image']

class ProductReviewSerliazer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['user','rate','review','created_at']

class ProductListSerializer(TaggitSerializer,serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = ['tags','name','flag','price','image','sku','subtitle','description','brand','slug','review_count','avg_rate']
   

class ProductDetailSerializer(TaggitSerializer,serializers.ModelSerializer):
     brand = serializers.StringRelatedField()
     image = ProductImageSerliazer(source='product_image',many=True)
     reviews = ProductReviewSerliazer(source='review_product',many=True)
     tags = TagListSerializerField()

     class Meta:
       model = Product
       fields = ['tags','name','reviews','image','flag','price','image','sku','subtitle','description','brand','slug','review_count','avg_rate']

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'