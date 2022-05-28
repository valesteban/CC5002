#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import sys
from db import DB
from datetime import datetime
import cgitb
import re

cgitb.enable()



print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')


form = cgi.FieldStorage()

#print(form)


def funcionValidadora(FS):
    """Funcion que recibe un FieldStorage y valida que esten correctas la informacion para luego ser agregada a la 
    base de datos"""

    #FieldStorage(None, None, [FieldStorage('sector', None, ''), FieldStorage('nombre', None, ''), 
    # FieldStorage('email', None, ''), FieldStorage('celular', None, ''), 
    # FieldStorage('contactar-por-link', None, ''), FieldStorage('dia-hora-inicio', None, '2022-05-05 13:58'), 
    # FieldStorage('dia-hora-termino', None, '2022-05-05 16:58'), FieldStorage('descripcion-evento', None, ''),
    #  FieldStorage('input', None, ''), FieldStorage('foto-actividad', '', b'')])
    errores = "Error en : <br>"
    
    #REGION
    if(not "region" in FS):
        errores = errores + "  No se ingresó una Región <br>"

    #COMUNA
    if(not "comuna" in FS):
        errores = errores + "  No se ingresó una Comuna <br>"
    
    #SECTOR
    sector = FS["sector"].value
    if(len(sector) > 100):
        errores = errores + "  Largo del Sector <br>"

    #NOMBRE
    nombre = FS["nombre"].value
    if(len(nombre) == 0 or len(nombre) > 200):
        errores = errores + "  Nombre <br>"
    
    #EMAIL
    email = FS["email"].value
    regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if( not re.fullmatch(regexEmail, email)):
        errores = errores + "  Email <br>"


    #CELULAR

    #arreglar
    celular = FS["celular"].value
    regexCelular = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-|.]?){6,7}$"
    if( (not re.fullmatch(regexCelular, celular) and len(celular)!= 0) or len(celular) > 12):
        errores = errores + "  Celular <br>"



    #CONTACTAR-POR
    if("contactar-po" in FS):
        ListaRS = FS['contactar-por']
        ListaConatto= FS['contactar-por-link']
        
        valCont = True
        if(len(ListaRS)>5 or len(ListaConatto)>5):
            valCont = False
    
        for urlcontacto in ListaConatto:
            urlc = urlcontacto.value
            if (len(urlc) > 50 or len(urlc) < 4 ):
                valCont = False
            print(urlcontacto.value)   

        if(valCont == False):
            errores = errores + "  Formas de Contacto <br>"

#MEF ALTA EL REGEX DE LA FECHA
    #DIA-HORA-INICIO
    inicio = FS["dia-hora-inicio"].value
    #print(inicio)

    inicioerror = True    
    if(len(inicio) == 0):
        inicioerror = False

    try:
        datetime.strptime(inicio, '%Y-%m-%d %H:%M')
    except ValueError:
        inicioerror = False

    if(inicioerror == False):
        errores = errores + "  Fecha Inicio <br>"


    #DIA-HORA-TERMINO
    tetrmino = FS["dia-hora-termino"].value

    terminoerror = True
    
    try:
        datetime.strptime(tetrmino, '%Y-%m-%d %H:%M')
    except ValueError:
        terminoerror = False

    if(terminoerror == False):
        errores = errores + "  Fecha Termino <br>"


    #DESCRIPCION-EVENTO
    descripcion = FS["descripcion-evento"].value


    #TEMA   #este es mas 
    temaerror = True
    if(not "tema" in FS):
        temaerror = False

    else:
        tema = FS["tema"].value
     #   print(tema)

        if (tema == "Otro"):
            temaInput = FS["input"].value
            if(len(temaInput) < 3 or len(temaInput) > 15 ):
                temaerror = False

    if(temaerror == False):
        errores = errores + "  Tema <br>"        


    #FOTO-ACTIVIDAD #este tambien es raro
    fotoerror = True
    if(not "foto-actividad" in FS):
        print("no ingresaste iamgenes")
        fotoerror = False
    
    else:
        Fotos = FS["foto-actividad"]
        if(type(Fotos) == list):
            if(len(Fotos) > 5):
                fotoerror = False
        
        #el resto de la validacion está dentro del metodo que guarda la foto en la bd

    if(fotoerror == False):
        errores = errores + "  Imagen <br>" 

    

    return errores




#---------------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------
def funcionArregla(form):
    """
    funcion que arregla los input para guardarlos en la base de datos
        y los guarda en la base de datos"""
    
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
        form["celular"] = None

    if (not "sector" in form):
        #print("no pusieron sector")
        form["sector"] = None  

    if (not "dia-hora-termino" in form):
        #print("no pusieron termino")
        form["dia-hora-termino"] = None 

    if (not "descripcion-evento" in form):
        #print("no pusieron descripcion")
        descripcionActib = None
    else:
        descripcionActib = form["descripcion-evento"].value  

    data_actividad = (     
        comunaId,
        form["sector"].value, 
        form["nombre"].value,
        form["email"].value,
        form["celular"].value,
        form["dia-hora-inicio"].value,
        form["dia-hora-termino"].value,
        descripcionActib,   
        ListaTemasP,
        ListaInputTemasP    
    )
    db.guardar_actividad(data_actividad) #<-----------------------------------------------------------------------

    #GUARDAR FORMAS DE CONTACTAR

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
        db.guardar_contactos(ListaContactos) #<-------------------------------------------------------------------------



    #GUARDAR FOTOS
    #Validacion está dentro del metodo que guarda en la base de datos la imagen
    fotos = form["foto-actividad"]
    #le paso solo las que tenga un nombre porque puede ocurrir que aprente el botos para agregar mas fotos pero no puse nada
    fotosSi = []
    #print(fotos)
    if (type(fotos) == list):
        for f in fotos:
         if(not f.filename == ""):
                fotosSi.append(f)
    else:
        fotosSi.append(fotos)  


    db.guardar_fotos(fotosSi) #<--------------------------------------------------------------------------------

err = funcionValidadora(form)    
if (len(err) > 16 ):
    mensaje = err + "<br><p> No se ha podido enviar la actividad</p> "

else:
    mensaje = "La informarción se ha guardado correctamente"
    funcionArregla(form)


enHead = """
        <link rel='stylesheet' href='../estilos/estilo1.css'>
        <script src='../mis-js/FunAct.js'></script>
        """

with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
        
    print(file.format('Enviado correctamente',enHead,"","Enviado Correctamente",
    f"""<div class= 'rectangulo_contenido'>
    {mensaje}
    </div>""" )) 
    