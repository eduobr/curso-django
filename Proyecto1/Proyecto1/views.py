from django.http import HttpResponse
import datetime as dt
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render

def saludo(request): #primara vista
    nombre = "Eduardo"
    apellido = "Obr"
    fec_actual = dt.datetime.now()

    #doc_externo=open("D:\Respaldo\curso-django\Proyecto1\Proyecto1\plantillas\miplantilla.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = loader.get_template('miplantilla.html')

    #puede recibir un diccionario
    #ctx = Context({"nombre_persona":nombre,"apellido_persona":apellido,"momento_actual":fec_actual,"temas":["Plantillas","Modelo","Formulario","Vistas","Despliegue"]})
    #sin usar el cargador de plantilla
    #documento = plt.render(ctx)

    #usando cargador de plantilla le debemos pasar directamente el diccionario
    #documento=doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido,"momento_actual":fec_actual,"temas":["Plantillas","Modelo","Formulario","Vistas","Despliegue"]})
    #return HttpResponse(documento)
    return render(request,"miplantilla.html",{"nombre_persona":nombre,"apellido_persona":apellido,"momento_actual":fec_actual,"temas":["Plantillas","Modelo","Formulario","Vistas","Despliegue"]})
    #return HttpResponse("<h1>Esta es mi primera página con Django</h1>")

def despedida(request): #primara vista
    return HttpResponse("Esta es mi primera página con Django")

def dameFecha(request):
    fecha_actual=dt.datetime.now()
    documento = "<h1>Fecha y Hora actuales: %s </h1>" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno):
    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento = "En el año %s tendrás %s años" % (agno,edadFutura)
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual = dt.datetime.now()
    return render(request,"curso-c.html",{"dameFecha":fecha_actual})
