from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    return HttpResponse("Ruta para probar la creación de modelos")


