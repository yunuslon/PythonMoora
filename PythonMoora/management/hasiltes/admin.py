from django.contrib import admin
from orm.models import Hasiltes

class HasiltesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hasiltes, HasiltesAdmin)
