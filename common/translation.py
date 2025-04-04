from modeltranslation.translator import translator, TranslationOptions
from .models import Contacts

class ContactsTranslationOptions(TranslationOptions):
    fields = ('address', )

translator.register(Contacts, ContactsTranslationOptions)
