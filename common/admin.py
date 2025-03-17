from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from common.models import Footer
@admin.register(Footer)

class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass