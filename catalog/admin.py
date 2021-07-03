from category.models import Category
from django.contrib import admin
from catalog.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'slug', 'public_price',
                    'is_available', 'created_at', 'updated_at', 'category', 'expire_at', 'internal_price' ]
    list_filter = [ 'is_available', 'created_at', 'updated_at' ]
    list_editable = [ 'public_price', 'is_available' ]
    prepopulated_fields = { 'slug' : ( 'name' , ) }
