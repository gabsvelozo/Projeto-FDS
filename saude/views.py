from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import HistoricoMedico, SintomasUsuario
from django.contrib.auth import authenticate, login as lg, login
from django.contrib.auth.models import User
from saude.models import Especialidade, Local, Consulta
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class HistoricoOnline(View):
    def get(self, request):
        return render(request, 'historico_form.html')
    
    def post(self, request):
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        medicacao = request.POST.get("medicacao")
        doencas = request.POST.get("doencas")
        cirugias = request.POST.get("cirugias")
        alergias = request.POST.get("alergias")

        historico = HistoricoMedico(
            nome=nome, 
            idade=idade, 
            medicacao=medicacao, 
            doencas=doencas,
            cirugias=cirugias, 
            alergias=alergias
        )

        historico.save()

        return redirect('saude:menu')
    
class Sucesso(View):
    def get(self, request):
        return render(request, 'sucesso.html')

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):  
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            CadastroView.criarUsuario(username, email, password)
            return redirect('home')  
        except ValueError as e:
            return render(request, 'cadastro.html', {'error': str(e)})

    @staticmethod  
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
            return redirect('saude:home')  
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
            'nome': request.user,  
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
            especialidade_id=especialidade_id,
            local_id=local_id,
            data=data
        )
        consulta.save()
        return redirect('saude:menu')

class ConsultasView(View):
    def get(self, request):
        consultas = Consulta.objects.filter(usuario=request.user)
        return render(request, 'consultas.html', {'consultas': consultas})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Autenticado com sucesso.')
            return redirect('saude:menu')  
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
        return redirect('saude:menu')  
    
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
        return redirect('saude:registros')  

    return render(request, 'confirmar_exclusao.html', {'registro': registro})
    