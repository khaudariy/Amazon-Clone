from django.contrib import admin
from .models import Product,Brand,Review,ProductImage


class ProductImagesInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    search_fields = ('name', 'sku')
    #list_filter = ["Product"]


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)

# Register your models here.
