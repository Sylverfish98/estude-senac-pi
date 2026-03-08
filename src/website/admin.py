from django.contrib import admin

from .materia import Materia
from .topic import Topic


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario", "cor")
    list_filter = ("usuario",)
    search_fields = ("nome",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("nome", "materia", "data_estudo", "index", "is_completed")
    list_filter = ("is_completed", "data_estudo", "materia__usuario")
    search_fields = ("nome", "materia__nome")
    ordering = ("data_estudo", "materia", "index", "id")
