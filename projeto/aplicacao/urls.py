from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='cadastro'),
    path('inicial/', views.inicial, name='inicial'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastrarMotorista/', views.cadastrarMotorista, name='cadastrarMotorista'),
    path('informarAbastecimento/', views.informarAbastecimento, name='informarAbastecimento'),
    path('cadastroManutencao/', views.cadastroManutencao, name='cadastroManutencao'),
    path('informarManutencao/', views.informarManutencao, name='informarManutencao'), 
    path('gerarRelatorio/', views.gerarRelatorio, name='gerarRelatorio'),
    path('acessarVeiculo/', views.acessarVeiculo, name='acessarVeiculo'),
    path('cadastroVeiculo/', views.cadastroVeiculo, name='cadastroVeiculo'),
    

    ]