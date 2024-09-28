from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as lg
from django.contrib.auth.models import User
from App.models import Especialidade, Local, Consulta

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):  # Corrigido 'sef' para 'self'
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            CadastroView.criarUsuario(username, email, password)
            return redirect('home')  # Corrigido para redirecionar para a URL nomeada
        except ValueError as e:
            return render(request, 'cadastro.html', {'error': str(e)})

    @staticmethod  # Adicionado @staticmethod para poder ser chamado sem instância
    def criarUsuario(username, email, password):
        if CadastroView.obterUsuarioPorNome(username) is not None:
            raise ValueError("Usuário já existe")
        else:
            user = User.objects.create_user(username, email, password)
            user.save()

    @staticmethod
    def obterUsuarioPorNome(name):
        return User.objects.filter(username=name).first()

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            LoginView.loginUsuario(request, username, password)
            return redirect('home')  # Corrigido para redirecionar para a URL nomeada
        except ValueError as e:
            return render(request, 'login.html', {'error': str(e)})

    @staticmethod
    def loginUsuario(request, username, password):
        user = authenticate(username=username, password=password)

        if user is None:
            raise ValueError("Usuário ou senha inválidos")
        else:
            lg(request, user)

class AgendamentoView(View):
    def get(self, request):
        especialidades = Especialidade.objects.all()
        locais = Local.objects.all()
        context = {
            'especialidades': especialidades,
            'locais': locais,
            'nome': request.user.username,  # Adiciona o nome do usuário
        }
        return render(request, 'agendamento.html', context)

    def post(self, request):
        especialidade_id = request.POST.get('especialidade')
        local_id = request.POST.get('local')
        data = request.POST.get('data')

        especialidade = Especialidade.objects.get(id=especialidade_id)
        local = Local.objects.get(id=local_id)

        consulta = Consulta(
            usuario=request.user,
            especialidade=especialidade,
            local=local,
            data=data
        )
        consulta.save()
        return redirect('consultas')

class ConsultasView(View):
    def get(self, request):
        consultas = Consulta.objects.filter(usuario=request.user)
        return render(request, 'consultas.html', {'consultas': consultas})
