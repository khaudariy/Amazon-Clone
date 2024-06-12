from typing import Any
from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Product, Brand , Review ,ProductImage
from django.db.models import Q , F , Value
from django.db.models.aggregates import Count,Sum,Avg,Max,Min
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 10


class ProductDetail(DetailView):
    model= Product  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] =  ProductImage.objects.filter(product = self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)                        
        return context  
    
class BrandList(ListView):
    model = Brand
    paginate_by = 50
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))

class BrandDetail(ListView):
    model = Product
    template_name ='products/brand_detail.html'
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
            
def add_review(request,slug):
    product = Product.objects.get(slug=slug)

    review = request.POST['review']
    rate = request.POST['rating']

    Review.objects.create(
        
        product = product,
        review = review,
        rate = rate
    )

    reviews = Review.objects.filter(product=product)
    page = render_to_string('includes/reviews.html',{'reviews':reviews})
    return JsonResponse({'result':page})
    #return redirect(f'/products/{slug}')


