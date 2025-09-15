from django.shortcuts import render
from .models import alunos

def home (request):
    todos_alunos = alunos.objects.all()
    return render (request, 'index.html', {'all':todos_alunos})
