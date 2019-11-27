from django.contrib import admin
from .models import Disciplina, Aluno, Professor, Matricula, Alocacao


@admin.register(Disciplina)
class admin_disciplina(admin.ModelAdmin):
    list_display = ['codigo', 'titulo']


@admin.register(Aluno)
class admin_aluno(admin.ModelAdmin):
    list_display = ['num_mat', 'nome']


@admin.register(Professor)
class admin_professor(admin.ModelAdmin):
    list_display = ['nfunc', 'nome', 'endereco_cidade', 'endereco_bairro',
                    'endereco_rua', 'endereco_numero', 'endereco_complemento', 'fone', 'titulacao']


@admin.register(Matricula)
class admin_matricula(admin.ModelAdmin):
    list_display = ['aluno', 'disciplina', 'ano', 'faltas', 'nota_final']


@admin.register(Alocacao)
class admin_alocacao(admin.ModelAdmin):
    list_display = ['professor', 'disciplina',
                    'ano_letivo', 'carga', 'horario']


# admin.site.register(Aluno)
# admin.site.register(Disciplina)
# admin.site.register(Professor)
# admin.site.register(Matricula)
# admin.site.register(Alocacao)
