from django.db import models
from datetime import datetime


class Aluno(models.Model):
    num_mat = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="* Nome do Aluno",
                            help_text="Insira o nome completo do Aluno, com limite de 100 caracteres.")

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="* Nome da Disciplina",
                              help_text="Insira o nome da Disciplina, com limite de 50 caracteres.")

    def __str__(self):
        return self.titulo


class Professor(models.Model):
    nfunc = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="* Nome do Professor",
                            help_text="Insira o nome completo do Professor, com limite de 100 caracteres.")
    endereco_cidade = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="* (Endereço) Cidade",
                                       help_text="Insira a cidade de moradia do Professor, com limite de 100 caracteres.")
    endereco_bairro = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="* (Endereço) Bairro",
                                       help_text="Insira o bairro de moradia do Professor, com limite de 100 caracteres.")
    endereco_rua = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="* (Endereço) Rua",
                                    help_text="Insira a rua de moradia do Professor, com limite de 100 caracteres.")
    endereco_numero = models.CharField(max_length=10, null=False, blank=False, default="", verbose_name="* (Endereço) Número",
                                       help_text="Insira o número da moradia do Professor, com limite de 10 caracteres.")
    endereco_complemento = models.CharField(max_length=50, default="Sem complemento", verbose_name=" (Endereço) Complemento",
                                            help_text="Insira o complemento da moradia do Professor, com limite de 50 caracteres.")
    fone = models.CharField(max_length=20, null=False, blank=False, default="(99) 99999-9999",
                            verbose_name="* Telefone do Professor", help_text="Insira o telefone do Professor.")
    titulacao = models.CharField(max_length=50, null=False, blank=False, default="", verbose_name="* Titulação do Professor",
                                 help_text="Insira a titulação do Professor, com limite de 50 caracteres.")

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    ano = models.IntegerField()
    faltas = models.IntegerField()
    nota_final = models.FloatField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome


class Alocacao(models.Model):
    ano_letivo = models.IntegerField()
    carga = models.IntegerField()
    horario = models.TimeField(auto_now=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.professor.nome
