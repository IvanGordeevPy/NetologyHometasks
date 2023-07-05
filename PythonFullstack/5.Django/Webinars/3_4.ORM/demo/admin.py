from django.contrib import admin
from .models import Person, Car, Product, Order, OrderPosition


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'color',]
    list_filter = ['brand', 'model',]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car',]

class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 3

@admin.register(Product)
class ProdictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline,]