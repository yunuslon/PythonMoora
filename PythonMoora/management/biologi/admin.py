from django.contrib import admin
from orm.models import Biologi

class BiologiAdmin(admin.ModelAdmin):
    pass
admin.site.register(Biologi, BiologiAdmin)
