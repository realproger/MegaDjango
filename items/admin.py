from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin
from .models import Item, Category, SubCategory, Characteristic, Cart, CartItem


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    inlines = [CharacteristicInline, ]

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Characteristic)
class CharacteristicInline(admin.TabularInline):
    model = Characteristic



# @admin.register(CartItem)
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]
    

