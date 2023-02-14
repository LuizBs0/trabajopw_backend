from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from .models import Usuario, Restaurante, Plato


# Create your views here.

def login(request):

    return 

def restaurantes(request):
    if request.method == 'GET':
        tipo = request.GET.get('tipo')

        if tipo == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        resFiltrados = []

        if tipo == "-1":
            restaurantes = Restaurante.objects.all()
        else:
            restaurantes = Restaurante.objects.filter(tipo_pk=tipo)

        for res in restaurantes:
            resFiltrados.append({

            })
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    return 

def platos(request):
    # if request.method == 'GET':
    
    return 

