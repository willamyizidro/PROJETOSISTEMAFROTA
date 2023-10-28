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
    discriminacao = forms.CharField(label="text",max_length=100)
    produto = forms.CharField(label="text",max_length=100)
    tempoTroca = forms.IntegerField(label="text")
    validadeporkm = forms.IntegerField(label="text")
    valor = forms.DecimalField(max_digits=2)



    

        


