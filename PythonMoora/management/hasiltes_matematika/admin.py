from django.contrib import admin
from orm.models import HasilTes_Matematika 

class HasilTes_MatematikaAdmin(admin.ModelAdmin):
    pass
admin.site.register(HasilTes_Matematika, HasilTes_MatematikaAdmin)
