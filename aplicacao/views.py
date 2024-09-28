from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import SintomasUsuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Autenticado com sucesso.')
            return redirect('menu')  
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')

    return render(request, 'login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Conta criada com sucesso! Faça login.')
                return redirect('login')  
        else:
            messages.error(request, 'As senhas não coincidem.')
    return render(request, 'cadastro.html')

@login_required  
def menu_view(request):
    return render(request, 'menu.html', {'username': request.user.username})

@login_required
def checklist_view(request):
    sintomas_comuns = ['Febre', 'Dor de cabeça', 'Dor de garganta', 'Tosse', 'Falta de ar', 'Cansaço', 
                       'Dor no corpo', 'Calafrios', 'Perda de olfato', 'Perda de paladar', 
                       'Congestão nasal', 'Diarreia', 'Náusea', 'Vômito', 'Dor abdominal']
    
    if request.method == 'POST':
        sintomas_selecionados = request.POST.getlist('sintomas')
        outros = request.POST.get('outros')
        periodo = request.POST.get('periodo')
        dor = request.POST.get('dor')  
        quando_dor = request.POST.get('quando_dor')
        algo_mais = request.POST.get('algo_mais')

        if outros:
            sintomas_selecionados.append(outros)

        if dor == '':
            dor = 0  
        else:
            dor = int(dor)  
        
        sintomas_usuario = SintomasUsuario(
            usuario=request.user, 
            sintomas=', '.join(sintomas_selecionados),
            periodo=periodo,
            dor=dor,
            quando_dor=quando_dor,
            algo_mais=algo_mais
        )
        sintomas_usuario.save()  
        
        messages.success(request, 'Seus sintomas foram enviados com sucesso!')
        return redirect('menu')  
    
    return render(request, 'checklist.html', {'sintomas_comuns': sintomas_comuns})


class sintomas_view(View):
    def get(self, request):
        lista_consultas = SintomasUsuario.objects.filter(usuario=request.user)
        context = {
            "lista_consultas": lista_consultas,
            "tem_registros": lista_consultas.exists(),  
        }
        return render(request, "registros.html", context)

@login_required
def delete_registro_view(request, id):
    registro = get_object_or_404(SintomasUsuario, id=id, usuario=request.user)

    if request.method == 'POST':
        registro.delete()  
        messages.success(request, 'Registro excluído com sucesso!')
        return redirect('registros')  

    return render(request, 'confirmar_exclusao.html', {'registro': registro})
