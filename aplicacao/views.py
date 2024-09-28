from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
