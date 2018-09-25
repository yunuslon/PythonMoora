from django.contrib import admin
from orm.models import Kimia

class KimiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kimia, KimiaAdmin)
