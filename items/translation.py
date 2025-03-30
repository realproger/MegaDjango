from modeltranslation.translator import translator, TranslationOptions
from .models import Item, Characteristic

class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

# class CharacteristicTranslationOptions(TranslationOptions):
#     fields = ('text',)

translator.register(Item, ItemTranslationOptions)
# translator.register(Characteristic, CharacteristicTranslationOptions)