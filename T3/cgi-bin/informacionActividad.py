#!/usr/bin/python3
# -*- coding: utf-8 -*-
from ast import arg
import sys
import math
from db import DB
import cgi

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')

argumentos = cgi.FieldStorage() #FieldStorage(None, None, [MiniFieldStorage('id', '2')])
idActividad = argumentos["id"].value

#print("id actividad",idActividad,"\n")

#OBTENEMOS LA ACTIVIDAD DE LA BASE DE DATOS
actividad = db.obtener_actividad_por_id(idActividad)
#print("actividad bd:", actividad,"\n")
comunaid= actividad[0][1]
comunaActInfo = db.obtener_comuna_por_id(comunaid)  #[(60107, 'Doñihue', 6)]     id nombre idregion

#OBTENER POR EL ID
region = db.obtener_region_por_id(comunaActInfo[0][2]) #[(6, 'Región del Libertador Bernardo Ohiggins')]

#OBTENER LAS FORMAS DE CONTACTO
Listacontactos = db.obtener_contacto_por_actividad_id(idActividad)
inputContactos = ""
#[(7, 'twitter', 'MatíasCordóntwitter', 2), (8, 'telegram', 'MatíasCordóntelegram', 2)]
if(len(Listacontactos)==0):
    inputContactos = " No Hay Información"
else:
    for cont in Listacontactos:
        linea = f"""
                <p>{cont[1]} : {cont[2]}<p>"""
        inputContactos = inputContactos+linea            


#OBTENER IMAGENES
Listaimagenes = db.obtener_imagen_por_id(idActividad)
inputima = ""
for ima in Listaimagenes:
    pathIma = ima[1]
    lineai = f"""
        <img src= "../imagenes/{pathIma}" width='250' height='150' alt='Imagen Actividad'  onclick="ver_imagen('{pathIma}')">
   
        """
    inputima = inputima + lineai    


contenido = f"""
        <div class= "rectangulo_contenido 1">
            <div class="caja_form" >
                <p>Inicio: {str(actividad[0][6])}</p>
                <p>Termino: {str(actividad[0][7])}</p>
                <p>Región: {str(region[0][1])} </p> 
                <p>Comuna: {str(comunaActInfo[0][1])}</p>
                <p>Sector: {str(actividad[0][2])}</p>
                <p>Tema: {str(actividad[0][8])}</p>
                <p>Nombre Organizador: {str(actividad[0][3])}</p>
                <p>Email: {str(actividad[0][4])}</p>
                <p>Celular: {str(actividad[0][5])}</p>
                <p>Contacto:{str(inputContactos)}</p>
                <p>Descripción: {str(actividad[0][8] if len(actividad[0][8])!=0 else "No Hay información" )}</p>
                <p> Fotos :</p><br>
                {inputima}
            </div>
        """
        

enHead = """
        <link rel='stylesheet' href='../estilos/estilo1.css'>
        <script src='../mis-js/paginas.js'></script>
        """

with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
    
    print(file.format('Listado Actividades', enHead,"","Listado Actividades",
    f"""
    <div  id = "light_box1" class= "activo ">
    <div class="en-grande ">

    </div>
    <div class="contenido">
        <div class="en-grande "></div>
        <div class="titulo"> Información Evento </div>
        {contenido}
        
        <button onclick='window.location.href = "listadoActividades.py" '>Volver al Listado</button>
        <button onclick='window.location.href = "portada.py" '>Volver al Inincio</button></div>
    </div>
</div>
    
      
"""))