from django.shortcuts import render
from .models import Pariente
# Create your views here.

def show_index(request):
    padre = Pariente(nombre='Juan', apellido='Hnatiuk', parentesco='padre', edad=62)
    madre = Pariente(nombre='Silvana', apellido='Potenza', parentesco='madre', edad=58)
    hermana = Pariente(nombre='Agustina', apellido='Hnatiuk', parentesco='hermana', edad=30)
    hermano = Pariente(nombre='Marcos', apellido='Hnatiuk', parentesco='hermano', edad=34)

    return render(request, 'index.html', {'objetos': [padre, madre, hermana, hermano]})
