from django.urls import path
from . import views

app_name = 'Saude'

urlpatterns = [
    path('historico/', views.HistoricoOnline.as_view(), name='historico'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
]