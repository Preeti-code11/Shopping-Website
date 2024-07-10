from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'locality', 'city', 'zipcode', 'state')
    search_fields = ('user__username', 'name', 'city', 'state')
    list_filter = ('state', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'brand', 'category')
    search_fields = ('title', 'brand', 'category')
    list_filter = ('brand', 'category')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('user__username', 'product__title')
    list_filter = ('user',)

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status')
    search_fields = ('user__username', 'customer__name', 'product__title')
    list_filter = ('status', 'ordered_date')

# Alternatively, you can register the models without custom admin classes:
# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(OrderPlaced)

