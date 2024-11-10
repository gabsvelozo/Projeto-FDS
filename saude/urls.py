from django.urls import path
from saude.views import AgendamentoView, ConsultasView, LocalView, Locais_PostoView
from . import views

app_name = 'saude'

urlpatterns = [
    path('', views.login_view, name='login'), 
    path('cadastro/', views.cadastro_view, name='cadastro'),  
    path('menu/', views.menu_view, name='menu'),
    path('historico/', views.HistoricoOnline.as_view(), name='historico_form'),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
    path('consultas/', ConsultasView.as_view(), name='consultas'),  
    path('checklist/', views.checklist_view, name='checklist'),
    path('registros/', views.sintomas_view.as_view(), name='registros'), 
    path('registros/delete/<int:id>/', views.delete_registro_view, name='delete_registro'),
    path('localizacao/', LocalView.as_view(), name='localizacao'),
    path('localizacao/', Locais_PostoView.as_view(), name='vacinas'),
]