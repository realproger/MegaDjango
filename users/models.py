from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
    def __str__(self):
        return self.username