from django.contrib import admin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin
from .models import Item, Category, SubCategory, Characteristic, Cart, CartItem

# @admin.register(Characteristic)
class CharacteristicInline(TabularInline):
    model = Characteristic


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [CharacteristicInline, ]

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass

# @admin.register(CartItem)
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]
    
# admin.site.register(Item, ItemAdmin)
