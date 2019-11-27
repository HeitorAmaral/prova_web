from django.contrib import admin
from .models import Disciplina, Aluno, Professor, Matricula, Alocacao

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Matricula)
admin.site.register(Alocacao)
