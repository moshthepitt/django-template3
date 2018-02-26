from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class FlatPageCustom(FlatPageAdmin):
    pass


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
