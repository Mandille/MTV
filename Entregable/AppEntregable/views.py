from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio(request):
    return HttpResponse("Entrega MTV")

def familiares(request):
    lista=[["Edgardo","Mandille","55","18/11/1967"], ["Rosa Elena","Tealdi","54","05/07/1968"],["Geronimo","Mandille","18","03/05/2004"]]
    diccionario={"familiares" : lista}
    plantilla= loader.get_template("entregable.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)


