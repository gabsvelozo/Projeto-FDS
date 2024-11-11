from django.contrib import admin # type: ignore
from .models import Especialidade, Local, Consulta, SintomasUsuario, Bairros, Locais, Info_local, Locais_doencas

admin.site.register(Especialidade)
admin.site.register(Local)
admin.site.register(Consulta)
admin.site.register(SintomasUsuario)
admin.site.register(Bairros)
admin.site.register(Locais)
admin.site.register(Locais_doencas)
admin.site.register(Info_local)