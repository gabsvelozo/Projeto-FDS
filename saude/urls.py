from django.urls import path
from saude.views import AgendamentoView, ConsultasView, LocalView
from . import views

app_name = 'saude'

urlpatterns = [
    path('historico/', views.HistoricoOnline.as_view(), name='historico'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
    path('consultas/', ConsultasView.as_view(), name='consultas'),  
    path('menu/', views.menu_view, name='menu'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('registros/', views.sintomas_view.as_view(), name='registros'), 
    path('registros/delete/<int:id>/', views.delete_registro_view, name='delete_registro'),
    path('historico/', views.HistoricoOnline.as_view(), name='historico_form'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
    path('', views.login_view, name='login'), 
    path('cadastro/', views.cadastro_view, name='cadastro'),  
    path('localizacao/', LocalView.as_view(), name='localizacao'),
]