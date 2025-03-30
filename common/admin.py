from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.models import Footer, Contacts
@admin.register(Footer)

class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Contacts)
class SiteContactsAdmin(SingletonModelAdmin):
    fieldsets = ('Основная информация', {
            'fields': ('company_name', 'address', 'phone', 'email', 'working_hours')
        }),