from django.contrib import admin
from orm.models import Fisika

class FisikaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fisika, FisikaAdmin)
