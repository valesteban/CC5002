#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import cgi
import cgitb
cgitb.enable()
from db import DB

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'cc500276_u', 'nguesemvit', 'cc500276_db')


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
    





with open('../templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
    
    print(file.format('Portarda', "../estilos/estilo1.css","../FunAct.js","","Inicio",
    f"""<div class= 'rectangulo_contenido'>
        <p> ¡¡¡BIENVENIDES!!! a esta comunidad en la cual podrás tanto encontrar como registrar activiades.
        </p>
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
    </div>"""))
    