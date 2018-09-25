from django.contrib import admin
from orm.models import HasilTes_Fisika 

class HasilTes_FisikaAdmin(admin.ModelAdmin):
    pass
admin.site.register(HasilTes_Fisika, HasilTes_FisikaAdmin)
