# Generated by Django 4.2.6 on 2023-10-28 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0002_motorista'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=15)),
                ('tempoTroca', models.IntegerField()),
                ('kmTroca', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('chassi', models.CharField(max_length=17)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=15)),
                ('tara', models.IntegerField()),
                ('tamanho', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='motorista',
            name='endereco',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAtual', models.DateField()),
                ('kmAtual', models.IntegerField()),
                ('dataProximaMan', models.DateField(blank=True, null=True)),
                ('kmProximaMan', models.IntegerField(blank=True, null=True)),
                ('manutencao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacao.tipomanutencao')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacao.veiculo')),
            ],
        ),
    ]
