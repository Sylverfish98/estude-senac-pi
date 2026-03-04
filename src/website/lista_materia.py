from django.contrib import admin
from .materia import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'cor')
    list_filter = ('usuario',)
    search_fields = ('nome')
