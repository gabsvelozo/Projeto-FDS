from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),  
    path('menu/', views.menu_view, name='menu'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('registros/', views.sintomas_view.as_view(), name='registros'), 
    path('registros/delete/<int:id>/', views.delete_registro_view, name='delete_registro'),
    
]