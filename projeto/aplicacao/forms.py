from django import forms
from .models import *

class UsuarioForm(forms.Form):
    nome = forms.CharField(label="nome", max_length=50)
    usuario = forms.CharField(label="usuario", max_length= 30)
    email = forms.EmailField(label="email", max_length=50, widget=forms.EmailInput)
    senha = forms.CharField(label="senha", max_length=30, min_length=8,  widget=forms.PasswordInput)
    conf_senha = forms.CharField(label="senha", max_length=30 , min_length=8,  widget=forms.PasswordInput)


class LoginForm(forms.Form):
    usuario = forms.CharField(label="usuario", max_length= 30)
    senha = forms.CharField(label="senha", max_length=30, min_length=8,  widget=forms.PasswordInput)

class mudarSenhaForm(forms.Form):
    usuario = forms.CharField(label="usuario", max_length= 30)
    email = forms.EmailField(label="email", max_length=50 )
    senha = forms.CharField(label="senha", max_length=30, min_length=8,  widget=forms.PasswordInput)
    conf_senha = forms.CharField(label="conf_senha", max_length=30, min_length=8,  widget=forms.PasswordInput)


class MotoristaForm(forms.Form):
    nome = forms.CharField(label="text", max_length=50)
    endereco = forms.CharField(label='text', max_length=70)
    cnh = forms.CharField(label="text", max_length=5 )


class TipoManutencoesForms(forms.Form):
    produto = forms.CharField(label="text",max_length= 30)
    tempoTroca = forms.IntegerField()
    kmTroca = forms.IntegerField()
    valor = forms.DecimalField()

class VeiculoForms(forms.Form):
    placa = forms.CharField(max_length=7, min_length=7)
    chassi = forms.CharField(max_length=17, min_length=17)
    marca = forms.CharField(max_length= 15)
    modelo = forms.CharField(max_length= 15)
    tara = forms.IntegerField()
    tamanho = forms.IntegerField()


class InformarManutencaoForm(forms.ModelForm):
    dataAtual = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Manutencao
        fields = ['manutencao', 'veiculo', 'dataAtual', 'kmAtual', 'dataProximaMan', 'kmProximaMan']
     

    def __init__(self, *args, **kwargs):
        super(InformarManutencaoForm, self).__init__(*args, **kwargs)
        self.fields['manutencao'].queryset = TipoManutencao.objects.all()
        self.fields['veiculo'].queryset = Veiculo.objects.all()

    
class InformarAbastecimentoForms(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    litros = forms.DecimalField(max_digits=5, decimal_places=2)
    kmatual = forms.IntegerField()

    class Meta:
        model = Abastecimentos
        fields = ['veiculo', 'data', 'litros', 'kmatual']

    def __init__(self, *args, **kwargs):
        super(InformarAbastecimentoForms, self).__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()






    

        


