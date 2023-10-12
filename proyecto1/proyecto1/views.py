from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

def formulario(request): #primera visita

    doc_externo=open("/home/usuario/Documentos/proyectos_django/proyecto1/proyecto1/plantillas/formulario.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)
    
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")


def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad, anio):

    #edadActual=18
    periodo=anio-2023
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendràs %s años" %(anio, edadFutura)

    return HttpResponse(documento)

