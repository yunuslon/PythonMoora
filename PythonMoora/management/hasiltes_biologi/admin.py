from django.contrib import admin
from orm.models import HasilTes_Biologi 

class HasilTes_BiologiAdmin(admin.ModelAdmin):
    pass
admin.site.register(HasilTes_Biologi, HasilTes_BiologiAdmin)
