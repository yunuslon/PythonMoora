from django.contrib import admin
from orm.models import Matematika

class MatematikaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Matematika, MatematikaAdmin)
