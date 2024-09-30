from django.contrib import admin
from .models import Especialidade, Local, Consulta, SintomasUsuario

admin.site.register(Especialidade)
admin.site.register(Local)
admin.site.register(Consulta)
admin.site.register(SintomasUsuario)