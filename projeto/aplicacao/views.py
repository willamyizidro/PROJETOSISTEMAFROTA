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



@login_required
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

@login_required
def cadastroManutencao(request):
    if request.method == "GET":
        return render(request ,'home/manutencao/cadastroManutencao.html', {"form": TipoManutencoesForms})
    else:
        manutAux = TipoManutencoesForms(request.POST)
        if manutAux.is_valid():
            manut = TipoManutencao()
            manut.produto = manutAux.cleaned_data['produto']
            manut.tempoTroca = manutAux.cleaned_data['tempoTroca']
            manut.kmTroca = manutAux.cleaned_data['kmTroca']
            manut.valor = manutAux.cleaned_data['valor']
            manut.save()
            messages.success(request, 'Manutenção salva.', extra_tags='sucess-message')
            return redirect('cadastroManutencao')
        else:
            messages.error(request, 'Confira os dados e tente novamente', extra_tags='error-message')
            return render(request ,'home/manutencao/cadastroManutencao.html', {"form": TipoManutencoesForms})


@login_required
def cadastroVeiculo(request):
    if request.method == "GET":
        return render(request ,'home/veiculo/cadastroVeiculo.html', {"form": VeiculoForms})
    else:
        veicAux = VeiculoForms(request.POST)
        if veicAux.is_valid():
            veiculo = Veiculo()
            veiculo.placa = veicAux.cleaned_data['placa']
            veiculo.chassi = veicAux.cleaned_data['chassi']
            veiculo.marca = veicAux.cleaned_data['marca']
            veiculo.modelo = veicAux.cleaned_data['modelo']
            veiculo.tara = veicAux.cleaned_data['tara']
            veiculo.tamanho = veicAux.cleaned_data['tamanho']
            veiculo.save()
            messages.success(request, 'Veiculo salvo.', extra_tags='sucess-message')
            return redirect('cadastroVeiculo')
        else:
            messages.error(request, 'Confira os dados e tente novamente', extra_tags='error-message')
            return render(request ,'home/manutencao/cadastroManutencao.html', {"form": VeiculoForms})
        

@login_required
def informarManutencao(request):
    if request.method == "GET":
        return render(request ,'home/manutencao/informarManutencao.html', {"form": InformarManutencaoForm})
    else:
        manutAux = InformarManutencaoForm(request.POST)
        if manutAux.is_valid():
            manut = Manutencao()
            manut.manutencao = manutAux.cleaned_data['manutencao']
            manut.veiculo = manutAux.cleaned_data['veiculo']
            manut.dataAtual = manutAux.cleaned_data['dataAtual']
            manut.kmAtual = manutAux.cleaned_data['kmAtual']
            manut.save()

            messages.success(request, 'Manutenção Salva.', extra_tags='sucess-message')
            return redirect('informarManutencao')
        else:
            messages.error(request, 'Confira os dados e tente novamente', extra_tags='error-message')
            return render(request ,'home/manutencao/informarManutencao.html', {"form": VeiculoForms})



@login_required
def informarAbastecimento(request):
    if request.method == "GET":
        return render(request ,'home/abastecimento/informarAbastecimento.html', {"form": InformarAbastecimentoForms})
    else:
        abast = InformarAbastecimentoForms(request.POST)
        if abast.is_valid():
            abastecimento = Abastecimentos()
            abastecimento.veiculo = abast.cleaned_data['veiculo']
            abastecimento.data = abast.cleaned_data['data']
            abastecimento.litros = abast.cleaned_data['litros']
            abastecimento.kmatual = abast.cleaned_data['kmatual']
            abastecimento.save()

            messages.success(request, 'Abatecimento Salvo.', extra_tags='sucess-message')
            return redirect('informarAbastecimento')
        else:
            messages.error(request, 'Confira os dados e tente novamente', extra_tags='error-message')
            return render(request ,'home/abastecimento/informarAbastecimento.html', {"form": InformarAbastecimentoForms})




def gerarRelatorio(request):
    return render(request ,'home/relatorios/gerarRelatorio.html')

def acessarVeiculo(request):
    return render(request ,'home/veiculo/acessarVeiculo.html')

