from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    search_fields = ("titulo", "contenido", "autor")
    list_filter = ("estado", "fecha_creacion")
    list_editable = ("estado",)
    prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(Post, PostAdmin)

# Register your models here.
