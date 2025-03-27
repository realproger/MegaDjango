from django.shortcuts import render
from items.models import Category, Item, SubCategory
def get_category(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_available=True)
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, context=context, template_name="base.html")

def get_subcategory(request, id):
    sub_categories = SubCategory.objects.get(Category = id)
    context = {
        'subcategories': sub_categories
    }
    


    