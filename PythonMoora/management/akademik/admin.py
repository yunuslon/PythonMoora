from django.contrib import admin
from orm.models import Akademik 

class AkademikAdmin(admin.ModelAdmin):
    pass
admin.site.register(Akademik, AkademikAdmin)
