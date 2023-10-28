from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from .consultas import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout 




def home(request):
   
    if request.method == "POST":
        useraux = UsuarioForm(request.POST)
        
        if useraux.is_valid():
            nome = useraux.cleaned_data['nome']
            username = useraux.cleaned_data['usuario']
            emailuse = useraux.cleaned_data['email']
            senha = useraux.cleaned_data['senha']
            confsenha = useraux.cleaned_data['conf_senha']
            user = User.objects.filter(username = username ).first()

            if  user:
                messages.error(request, 'Usuário ja existe!.', extra_tags='error-message')
                return render(request, 'home/cadastro.html', {"form": useraux })
            else:
                email = User.objects.filter(email = emailuse ).first()

                if email:
                    messages.error(request, 'Email já cadastrado!.', extra_tags='error-message')
                    return render(request, 'home/cadastro.html', {"form": useraux })
                else:
                    if senha != confsenha:
                        messages.error(request, 'Senhas não coincidem.', extra_tags='error-message')
                        return render(request, 'home/cadastro.html', {"form": useraux})
                    else:
                        user2 = User.objects.create_user(username=username,email=emailuse,password=senha, first_name = nome)
                        user2.save()
                        messages.success(request, 'Cadastro realizado com sucesso! Realize Login.', extra_tags='success-message')
                        return render(request, 'home/cadastro.html', {"form": UsuarioForm})

           
       
               
    return render(request, 'home/cadastro.html', {"form": UsuarioForm})


def login(request):
    if request.method == "GET":
        return render(request, 'registration/login.html', {"form": LoginForm})
    else:
        login = LoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data['usuario']
            senha = login.cleaned_data['senha']

            user = authenticate(username=username, password = senha)

            if user:
                login_django(request,user)
            else:
                messages.error(request, 'Usuario ou senha Invalidos.', extra_tags='error-message')
                return render(request, 'accounts/login.html', {"form": LoginForm})
        



@login_required
def inicial(request):
    return render(request, 'home/inicial.html')




def cadastrarMotorista(request):
    if request.method == "GET":

        return render(request, 'home/motorista/cadastrarMotorista.html', {"form": MotoristaForm})
    else:
        motaux = MotoristaForm(request.POST)
        if motaux.is_valid():
            mot = Motorista()
            mot.nome = motaux.cleaned_data['nome']
            mot.endereco =  motaux.cleaned_data['endereco']
            mot.cnh = motaux.cleaned_data['cnh']
            mot.save()
            messages.success(request, 'Cadastro salvo.', extra_tags='sucess-message')
            return redirect('cadastrarMotorista')
            
     
    return render(request, 'home/motorista/cadastrarMotorista.html', {"form": MotoristaForm})



def informarAbastecimento(request):
    return render(request ,'home/abastecimento/informarAbastecimento.html')

def cadastroManutencao(request):
    return render(request ,'home/manutencao/cadastroManutencao.html')

def informarManutencao(request):
    return render(request ,'home/manutencao/informarManutencao.html')

def gerarRelatorio(request):
    return render(request ,'home/relatorios/gerarRelatorio.html')

def acessarVeiculo(request):
    return render(request ,'home/veiculo/acessarVeiculo.html')

def cadastroVeiculo(request):
    return render(request ,'home/veiculo/cadastroVeiculo.html')
