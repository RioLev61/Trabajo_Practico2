from django.contrib import admin
from cac.models import Posteo, Usuario ,Categoria, Proyecto, Comentario
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class UsuarioAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'apellido')
    list_editable = ('apellido',)
    search_fields = ['nombre', 'apellido']


#mi_admin = CacAdminSite(name='cacadmin')
#mi_admin.register(Posteo,PosteoAdmin)
admin.site.register(Posteo)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Comentario)
#mi_admin.register(Categoria, CategoriaAdmin)
