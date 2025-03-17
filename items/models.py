from django.db import models
from ckeditor.fields import RichTextField


class User(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=12)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=1)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('order', )
    
    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField("Название категории", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=1)
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ('order', )
    
    def __str__(self):
        return self.name  
    
    
class Item(models.Model):
    user = models.ManyToManyField(User, related_name="Items")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='items', null=True)
    image = models.ImageField(verbose_name="Главная картинка товара", upload_to="items/img_box")
    title = models.CharField(verbose_name="Заголовок товара", max_length=255)
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2)
    production = models.CharField(verbose_name="Производство", max_length=255)
    model = models.CharField(verbose_name="Модель", max_length=255)
    is_available = models.BooleanField(verbose_name="Наличие", default=False)
    color = models.CharField("Цвет", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=1)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("order", )

class Characteristic(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='characteristic')
    text = RichTextField("Текст характеристики")
    
    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.item.title