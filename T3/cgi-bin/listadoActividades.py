#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
from db import DB
import cgi

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')
#data = db.get_data()

todasActividades = db.obtener_todas_actividades()
cantidadDivPaginas = math.ceil(len(todasActividades)/5 )  #cantidad de div que serán las paginas que apareceran y desapareceran
#print(cantidadDivPaginas)
#print(todasActividades)
divsPag = ""
for i in range(cantidadDivPaginas):  #creo un div por cada itrwacion

    #para que parta el primero activo y los de mas desactivos
    if (i == 0):
        nombre_clase = "activo"
    else:
        nombre_clase = "no_activo"

    inicio = i*5
    if(len(todasActividades)< i*5+5):
        fin = len(todasActividades)
    else:
        fin = i*5+5
    contenido5 = ""
    for j in range(inicio,fin):
        imagenes = db.obtener_imagen_por_id(todasActividades[j][0])
        path = imagenes[0][1]
        
        comuna = db.obtener_comuna_por_id(todasActividades[j][1]) #le paso el id de la comuna
        
        nuevo = f"""
                    <tr onclick="redirigirPag({todasActividades[j][0]})">
                        <td>{str(todasActividades[j][6])}</td>
                        <td>{str(todasActividades[j][7])}</td>
                        <td> {comuna[0][0]} </td>
                        <td>{str(todasActividades[j][2])}</td>
                        <td>{str(todasActividades[j][8])}</td>
                        <td>{str(todasActividades[j][3])}</td>
                        <td>{str(len(imagenes))} </td>
                        <td><img src= "../imagenes/{path}" width='250' height='150' alt='imagen escuela boxeo'></td>        
                    </tr>    
                """
        contenido5 = contenido5 +   nuevo     

    cincoactivdov = f"""
                    <div class= "rectangulo_contenido {str(nombre_clase)}" id="{str(i)}">
                        <table class='tabla_normal'>
                            <tr class="nombres-tabla">
                            <th> Inicio </th>
                            <th> Termino </th>
                            <th> Comuna </th>
                            <th> Sector </th>
                            <th> Tema </th>
                            <th> Nombre Organizador</th>
                            <th> Total Foto </th>
                            <th>  Foto </th>

                            {contenido5}
                        </table>
                    </div>        
                            """
    

        
    divsPag = divsPag +  cincoactivdov


enHead = """
        <link rel='stylesheet' href='../estilos/estilo1.css'>
        <script src='../mis-js/paginas.js'></script>
        """
        

with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
            
    print(file.format('Listado Actividades',enHead ,"","Listado Actividades",
    f"""
    
        
        {divsPag}

     
        <div>
            <button onclick= "anteriorBoton()"> Previo </button>
            <button onclick= "siguienteBoton({cantidadDivPaginas-1})"> Siguiente </button>
            <br>
            <button onclick='window.location.href = "portada.py" '>Volver al Inincio</button>
        </div>
"""))
    

    