from django.shortcuts import render
from .models import Aluno

def home(request):
    todos_alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': todos_alunos})
