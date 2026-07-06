from datetime import date
from django.shortcuts import render
from .models import Tarefa

def index(request):
    tarefas= Tarefa.objects.all()

    context = {
        'tarefas': tarefas,
        'hoje': date.today()
    }

    return render(request, 'tarefa/index.html', context)
