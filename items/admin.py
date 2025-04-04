from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin

from .models import Category, SubCategory, Item, Characteristic, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    # inlines = [CharacteristicInline, ]
    pass


# @admin.register(Characteristic)
class CharacteristicInline(admin.TabularInline):
    model = Characteristic


# @admin.register(CartItem)
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]
    

