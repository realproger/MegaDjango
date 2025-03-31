from modeltranslation.translator import translator, TranslationOptions
from .models import Item


class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Item, ItemTranslationOptions)

