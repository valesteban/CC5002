#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import cgi
import cgitb
cgitb.enable()
from db import DB
import json

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')


db = DB('localhost', 'root', '', 'tarea2')
#data = db.get_data()

ultimos5 = db.obtener_ultimas5_actividades()

#[(1, 'La Ligua', 'hnbgf', 'valentina', 'vale@gmail.cl', '+56950102497', datetime.datetime(2022, 5, 2, 16, 27), datetime.datetime(2022, 5, 2, 19, 27), 'Temaotro', 'Temaotro')]
cosasInsertar = ""
for actividad in ultimos5:
    #tego que crear una bsuqueda sql que me devuelva la comuna comuna = db.
    #tengo que hacer un abusqueda sql del path de la imagen
    #actividad = (2, 'Ñuñoa', 'Beauchef 850, terraza', 'Matías Cordón', 'MatiasCordon@gmail.com', '+569111024977', datetime.datetime(2022, 3, 23, 12, 0), datetime.datetime(2022, 5, 23, 14, 0), 'Escuela de Boxeo', 'Escuela de Boxe')
    imagen = db.obtener_imagen_por_id(actividad[0])[0]
    path = imagen[1]

    row = f"""  
         <tr>
                <td>{actividad[6]}</td>
                <td>{actividad[7]}</td>
                <td>{actividad[1]}</td>
                <td>{actividad[2]}</td>
                <td>{actividad[8]}</td> 
                <td><img src= "../imagenes/{path}" width='250' height='150' alt='imagen escuela boxeo'></td>
              
            </tr>

            """
    cosasInsertar = cosasInsertar+row    

#como todas las actividades si o si tendran imagenes 
listita = db.obtenerIdCOmunasActividades()

listitaComunas = []
for id in listita:
    comunaNombre = db.obtener_comuna_por_id(id)
    listitaComunas.append(comunaNombre[0][1])

with open('../') as file:
    data = json.load(file)



enHead = """
        <link rel='stylesheet' href='../estilos/estilo1.css'>
        <script src='../mis-js/FunAct.js'></script>

        
        <link rel="stylesheet" href="../leaflet/leaflet.css" />



        <!-- no pongo esto porq importe los documentos estan mas abajo 
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.8.0/dist/leaflet.css" integrity="sha512-hoalWLoI8r4UszCkZ5kL8vayOGVae1oxXe/2A4AO6J9+580uKHDO3JdHb7NzwwzK5xr/Fs0W40kiNHxM9vyTtQ==" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.8.0/dist/leaflet.js" integrity="sha512-BB3hKbKWOc9Ez/TAwyWxNXeoV9c1v6FIeYiBieIWkpLjauysF18NzgR1MBNBXf8/KABdlkX68nAhlwcDFLGPCQ==" crossorigin=""></script>
         -->
        """

with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
    
    print(file.format('Portarda',enHead ,"","Inicio",
    f"""<div class= 'rectangulo_contenido' id = 'contenido1'>
            <p> 
                ¡¡¡BIENVENIDES!!! a esta comunidad en la cual podrás tanto encontrar como registrar activiades.
                {listita}
                {listitaComunas}
            </p>
    </div>

    <div class= 'rectangulo_contenido'>
        <div class= 'rectangulo_contenido' id = 'map'>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br>

    </div>
    </div>

    <div class= 'rectangulo_contenido'>
    
    <table class='tabla_normal'>
        <tr class='nombres-tabla'>
            <th> Inicio </th>
            <th> Termino </th>
            <th> Comuna </th>
            <th> Sector </th>
            <th> Tema </th>
            <th> Foto </th>

            

         {cosasInsertar}

    </table>
    </div>
    </div>
    <script src="../leaflet/leaflet.js"></script>
    <script src= ../mis-js/mapa.js></script>
    """))
    