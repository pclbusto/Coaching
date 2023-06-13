from django.contrib import admin
from .models import Recurso,Info_Sesion

#admin.site.register(Recurso)



# Register your models here.
class RecursoAdmin(admin.ModelAdmin):
    list_display = ["dni", "apellido","nombre"]
    fields = ["apellido","nombre", "dni"]
class Info_SesionAdmin(admin.ModelAdmin):
    list_display = ["fecha", "hora","descripcion", "recurso"]
    list_filter = ["recurso"]

admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Info_Sesion, Info_SesionAdmin)
