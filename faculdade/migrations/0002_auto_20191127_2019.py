# Generated by Django 2.2.7 on 2019-11-27 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculdade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='end',
        ),
        migrations.AddField(
            model_name='professor',
            name='endereco_bairro',
            field=models.CharField(default='', help_text='Insira o bairro de moradia do Professor, com limite de 100 caracteres.', max_length=100, verbose_name='* (Endereço) Bairro do Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='endereco_cidade',
            field=models.CharField(default='', help_text='Insira a cidade de moradia do Professor, com limite de 100 caracteres.', max_length=100, verbose_name='* (Endereço) Cidade do Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='endereco_complemento',
            field=models.CharField(default='', help_text='Insira o complemento da moradia do Professor, com limite de 50 caracteres.', max_length=50, verbose_name=' (Endereço) Complemento do Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='endereco_numero',
            field=models.CharField(default='', help_text='Insira a o número da moradia do Professor, com limite de 10 caracteres.', max_length=10, verbose_name='* (Endereço) Número do Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='endereco_rua',
            field=models.CharField(default='', help_text='Insira a rua de moradia do Professor, com limite de 100 caracteres.', max_length=100, verbose_name='* (Endereço) Rua do Professor'),
        ),
    ]
