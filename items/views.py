from django.shortcuts import render, get_object_or_404
from items.models import Category, Item, SubCategory, Characteristic, Cart, CartItem

class TemplateService:

    def get_category(self):
        return Category.objects.all()

    def get_items(self):
        return Item.objects.all

    def get_subcategory(self, category_id):
        return SubCategory.objects.filter(category=category_id)
    
    def get_category(request):
        data = TemplateService()
        category = data.get_category()
        sub_category = data.get_subcategory()
        items = data.get_items()
        context = {
            "categories": category,
            "sub_categories": sub_category,
            "items": items
        }
        
        return render(request, context=context, template_name="base.html")