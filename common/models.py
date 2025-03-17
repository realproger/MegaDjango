from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Footer(models.Model):
    name = models.CharField("Название кнопки", max_length=50)
    description = RichTextField("Описание", null=True, blank=True)
    icon = models.ImageField("Иконка", upload_to="footer/icons", null=True, blank=True)
    link = models.TextField("Ссылка", null=True, blank=True)
    order = models.PositiveIntegerField("Порядок", default=1)
    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = verbose_name
        ordering = ('order',)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Footer, self).save(*args, **kwargs)





    