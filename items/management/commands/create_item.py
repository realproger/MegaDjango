from django.core.management import BaseCommand

from items.models import Item, SubCategory

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        items = Item.objects.filter(is_available=True, title='Iphone')
        for item in items:
            item.is_available = False
            item.save(update_fields=['is_available',])
        
        
        # sub_category = SubCategory.objects.get(id=2)
        # item = Item.objects.create(
        #     sub_category = sub_category,
        #     image = "C:/Users/user/Desktop/mega_django/items/img_box/iphone_12_pro_max.webp",
        #     title = "Iphone",
        #     description = "BEST SMARTPHONE",
        #     price = 100000,
        #     production = "Apple",
        #     model = "Iphone",
        #     is_available = True,
        #     color = "Midnight",
        # )
        # item.save()