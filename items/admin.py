from django.contrib import admin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin
from .models import Item, Category, SubCategory, Characteristic, User

# @admin.register(Characteristic)
class CharacteristicInline(TabularInline):
    model = Characteristic

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [CharacteristicInline, ]

@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass

# admin.site.register(Item, ItemAdmin)
