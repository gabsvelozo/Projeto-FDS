from django.contrib import admin
from .models import Especialidade, Local, Consulta, SintomasUsuario, Bairros, Locais

admin.site.register(Especialidade)
admin.site.register(Local)
admin.site.register(Consulta)
admin.site.register(SintomasUsuario)
admin.site.register(Bairros)
admin.site.register(Locais)