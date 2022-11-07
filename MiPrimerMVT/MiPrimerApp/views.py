from django.shortcuts import render

from MiPrimerApp.models import Familia
# Create your views here.


def mostrar_familia(request):

    a1 = Familia(nombre= 'Federico', apellido= 'Anton', edad=54, cumpleanios='1968-4-7')
    a2 = Familia(nombre= 'Ana', apellido= 'Leporace', edad=52, cumpleanios='1970-8-14')
    a3 = Familia(nombre= 'Julieta', apellido= 'Anton Leporace', edad=18, cumpleanios='2004-3-15')
    a4 = Familia(nombre= 'Joaquin', apellido= 'Anton Leporace', edad=22, cumpleanios='2000-8-20')

    return render (request, 'familia.html', {'familia':[a1, a2, a3, a4]})