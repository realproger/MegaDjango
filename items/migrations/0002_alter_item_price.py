# Generated by Django 5.1.7 on 2025-03-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
    ]
