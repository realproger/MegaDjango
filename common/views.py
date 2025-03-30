from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contacts
from solo.models import SingletonModel

def contacts_view(request):
    contacts = Contacts.get_solo()
    return render(request, 'base.html', {'contacts': contacts})
# Create your views here.
