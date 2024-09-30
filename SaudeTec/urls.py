"""
URL configuration for Saude project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Saude.views import HomeView, CadastroView, LoginView, AgendamentoView, ConsultasView
from Saude import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Saude.urls')),
    path('agendamento/', AgendamentoView.as_view(), name='agendamento'),
    path('consultas/', ConsultasView.as_view(), name='consultas'), 
    path('', views.login_view, name='login'),  
    path('cadastro/', views.cadastro_view, name='cadastro'),  
    path('menu/', views.menu_view, name='menu'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('registros/', views.sintomas_view.as_view(), name='registros'), 
    path('registros/delete/<int:id>/', views.delete_registro_view, name='delete_registro'),
    path('historico/', views.HistoricoOnline.as_view(), name='historico_form'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
]
