from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Restaurante, Plato, Categoria_Pla, Categoria_Res


#LOGIN TERMINADO
@csrf_exempt
def login(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest['usuario']
        password = dictDataRequest['password']

        
        try:
            usuarios = Usuario.objects.get(usuario=usuario, password=password)
            dictOK = {
                    "error": "",
                    "userid": usuarios.pk,
            }
            return HttpResponse(json.dumps(dictOK))
        except Usuario.DoesNotExist:
            dictError = {
                'error': 'No existe esa cuenta'
                }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        # if usuarios:
            
        # else:
            
    
        # for u in usuarios: 
        #     listaUsuarios.append({
        #             "id": u.pk,
        #             "nombre": u.usuario,
        #             "password": u.password
        #     })
        #     if u.usuario == usuario and u.password == password:
        #         dictOK = {
        #             'error': '',
        #             'userid': u.pk
        #         }
        #         return HttpResponse(json.dumps(dictOK))
        #     else:
        #         dictError = {
        #         'error': 'No existe esa cuenta',
        #         'usuarios': listaUsuarios
        #         }
        #         strError = json.dumps(dictError)
        #         return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest['usuario']
        password = dictDataRequest['password']        

        listaUsuarios = Usuario.objects.all()

        for u in listaUsuarios:
            if u.usuario == usuario:
                dictError = {
                'error': 'Usuario ya registrado'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
            else:
                newUsuario = Usuario(usuario=usuario, password=password)
                newUsuario.save()
                dictOK = {
                    'error': ''
                }
                return HttpResponse(json.dumps(dictOK))
    else:
            dictError = {
                'error': 'Tipo de peticion no existe'
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)



        


#CATEGORIA TERMINADO
def categoria_res(request):
    if request.method == 'GET':
        categorias = Categoria_Res.objects.all()
        listaCategorias = []

        for cat in categorias:
            listaCategorias.append({
                "id": cat.pk,
                "nombre": cat.nombre
            })
        
        dictResponse = {
            "error": "",
            "categorias": listaCategorias
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


#CATEGORIA TERMINADO
def categoria_pla(request):
    if request.method == 'GET':
        categorias = Categoria_Pla.objects.all()
        listaCategorias = []

        for cat in categorias:
            listaCategorias.append({
                "id": cat.pk,
                "nombre": cat.nombre
            })
        
        dictResponse = {
            "error": "",
            "categorias": listaCategorias
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
        
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
        

#RESTAURANTES TERMINADO
def restaurantes(request):
    if request.method == 'GET':
        categoria = request.GET.get('cat')

        if categoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        resFiltrados = []

        if categoria == "-1":
            restaurantes = Restaurante.objects.all()
        else:
            restaurantes = Restaurante.objects.filter(categoria__pk=categoria)

        for res in restaurantes:
            resFiltrados.append({
                "id" : res.pk,
                "nombre" : res.nombre,
                "horario" : res.horario,
                "descripcion" : res.descripcion,
                "categoria" : {
                    "id" : res.categoria.pk,
                    "nombre" : res.categoria.nombre
                }
            })

        dictResponse = {
            "error": "",
            "restaurantes": resFiltrados
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def listaUsuarios(request):
    if request.method == 'GET':
        categorias = Usuario.objects.all()
        listaCategorias = []

        for cat in categorias:
            listaCategorias.append({
                "id": cat.pk,
                "usuario": cat.usuario,
                "password": cat.password
            })
        
        dictResponse = {
            "error": "",
            "usuarios": listaCategorias
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

#PLATOS TERMINADO
def platos(request):
    if request.method == 'GET':
        restaurante = request.GET.get('res')
        categoria = request.GET.get('cat')

        if categoria == "-1":
            platos = Plato.objects.filter(restaurante_id__pk=restaurante)
        else:
            platos = Plato.objects.filter(restaurante_id__pk=restaurante, categoria__pk=categoria)

        plaFiltrados = []

        for pla in platos:
            plaFiltrados.append({
                "id" : pla.pk,
                "nombre" : pla.nombre,
                "precio" : pla.precio,
                "descripcion" : pla.descripcion,
                "categoria" : {
                    "id" : pla.categoria.pk,
                    "nombre" : pla.categoria.nombre
                }
            })

        dictResponse = {
            "error": "",
            "platos": plaFiltrados
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)



