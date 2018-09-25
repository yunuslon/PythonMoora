from django.contrib import admin
from orm.models import HasilTes_Kimia

class HasilTes_KimiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(HasilTes_Kimia, HasilTes_KimiaAdmin)
