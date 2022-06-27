# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
import cgi
import os
import sys
import filetype
from db import DB
import cgitb
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')
#data = db.get_data()

form = cgi.FieldStorage()

def funcionValidadora(FS):
    """Funcion que recibe un FieldStorage y valida que esten correctas la informacion para luego ser agregada a la 
    base de datos"""

    #REGION
    


    #COMUNA

    
    #SECTOR


    #NOMBRE


    #EMAIL


    #CELULAR


    #CONTACTAR-POR


    #DIA-HORA-INICIO


    #DIA-HORA-TERMINO


    #DESCRIPCION-EVENTO


    #TEMA


    #FOTO-ACTIVIDAD


# region comuna sector nombre email celular contactar-por contactar-por-link  
# dia-hora-inicio dia-hora-termino descripcion tema input foto

#FieldStorage(None, None, [MiniFieldStorage('region', 'Región de Antofagasta'),
#  MiniFieldStorage('comuna', 'Taltal'), MiniFieldStorage('sector', 'hnbgf'),
#  MiniFieldStorage('nombre', 'valentina'), MiniFieldStorage('email', 'vale@gmail.cl'), 
# MiniFieldStorage('celular', '+56950102497'), MiniFieldStorage('contactar-por', 'Telegram'),
#  MiniFieldStorage('contactar-por-link', 'tetet'), MiniFieldStorage('contactar-por', 'Instagram'),
#  MiniFieldStorage('contactar-por-link', 'instststst'), MiniFieldStorage('dia-hora-inicio', '2022-05-02 13:00'),
#  MiniFieldStorage('dia-hora-termino', '2022-05-02 16:00'), MiniFieldStorage('tema', 'Política'),
#  MiniFieldStorage('tema', 'Otro'), MiniFieldStorage('input', '2e23e'),
#  MiniFieldStorage('foto', 'tarea2.png'), MiniFieldStorage('foto', 'tarea2.png')])


comuna  =  form["comuna"].value
tupla = db.obtenerComunaIdRegioId(comuna)
comunaId = tupla[0][0] 
regionId = tupla[0][1] 

#GUARADR ACTIVIDAD

ListaTemas =  form['tema']                      #tema         puede ser mas de 1
ListaInputTemas =  form['input']
ListaTemasP = []
ListaInputTemasP = []

#print("temas",ListaTemas)
#print("temasinput",ListaInputTemas)

if(type(ListaTemas) is list):
    for tema in ListaTemas:
        if(tema.value != "Otro"):
            ListaTemasP.append(tema.value)
else:
    ListaTemasP.append(ListaTemas.value)
if(type(ListaInputTemas) is list):
    for temainput in ListaInputTemas:
        ListaInputTemasP.append(temainput.value)
else:
    ListaInputTemasP.append(ListaInputTemas.value)

#print(ListaTemasP)   # es una lista con todos los temas y aexistentes
#print(ListaInputTemasP)  #  es una lista con todos los nuevos temssd 

#como el celular es opcional lo pongo en null en caso que no venga
if (not "celular" in form):
    #print("no pusieron el celular")
    form["celular"] = NULL

if (not "sector" in form):
    #print("no pusieron sector")
    form["sector"] = NULL  

if (not "dia-hora-termino" in form):
    #print("no pusieron termino")
    form["dia-hora-termino"] = NULL 

if (not "descripcion" in form):
    #print("no pusieron descripcion")
    form["descripcion"] = NULL  

data_actividad = (     
    comunaId,
    form["sector"].value, 
    form["nombre"].value,
    form["email"].value,
    form["celular"].value,
    form["dia-hora-inicio"].value,
    form["dia-hora-termino"].value,
    form["descripcion"].value,   
    ListaTemasP,
    ListaInputTemasP    
)
#db.guardar_actividad(data_actividad) #<-----------------------------------------------------------------------

#GUARDAR FORMAS DE CONTACTAR

#if (not "contactar-por" in form):
    #print("no puso forma de econtactar")
    #form["contactar-por"] = NULL



if ( "contactar-por" in form): #si ouso frma de contactar , entonces guardamos en bd
    #print("si puso forma de contacto")
    contactos = form["contactar-por"]
    contactosLink = form["contactar-por-link"]
    ListaContactos = []
    #print("ddddddddddddd")
    #print(contactos=="")
    if(type(contactos) is list):
        for i,tema in enumerate(contactos):
            ListaContactos.append((tema.value,contactosLink[i].value))
    else:
        ListaContactos.append((contactos.value,contactosLink.value))

    #print(ListaContactos)     [('twiter', 'twtwtwite'), ('Telegram', 'tetet')]
#    db.guardar_contactos(ListaContactos) #<-------------------------------------------------------------------------



#GUARDAR FOTOS
#Validacion está dentro del metodo que guarda en la base de datos la imagen
fotos = form["foto"]
#le paso solo las que tenga un nombre porque puede ocurrir que aprente el botos para agregar mas fotos pero no puse nada
fotosSi = []
#print(fotos)
if (type(fotos) == list):
    for f in fotos:
        if(not f.filename == ""):
            fotosSi.append(f)
else:
    fotosSi.append(fotos)  


#db.guardar_fotos(fotosSi) #<--------------------------------------------------------------------------------



with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
    
    print(file.format('Enviado correctamente', "../estilos/estilo1.css","../FunAct.js","","Enviado Correctamente",
    f"""<div class= 'rectangulo_contenido'>

    Se Ha guardado correctamenete la información
    </div>""" )) 