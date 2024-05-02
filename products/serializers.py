from rest_framework import serializers
from .models import Product,Brand,Review,ProductImage




class ProductImageSerliazer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['image']

class ProductReviewSerliazer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['user','rate','review','created_at']

class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField(method_name='get_review_count')
    avg_rate = serializers.SerializerMethodField(method_name='get_avg_rate')
    class Meta:
        model = Product
        fields = '__all__'
    def get_avg_rate(self,object):
        total = 0 
        reviews = object.review_product.all()
        if len(reviews)>0:
            for item in reviews:
                total+=item.rate
            avg = total / len(reviews) 
        else:
            avg = 0      
        return avg 

    def get_review_count(self,object):
        reviews = object.review_product.all().count()
        return reviews    

class ProductDetailSerializer(serializers.ModelSerializer):
     brand = serializers.StringRelatedField()
     image = ProductImageSerliazer(source='product_image',many=True)
     reviews = ProductReviewSerliazer(source='review_product',many=True)
     class Meta:
       model = Product
       fields = '__all__' 
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'