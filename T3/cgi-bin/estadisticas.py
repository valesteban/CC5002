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


db = DB('localhost', 'root', '', 'tarea2')

enHead = """
            <link rel='stylesheet' href='../estilos/estilo1.css'>
            <script src='../mis-js/graficos.js'></script>
            <script src='https://code.highcharts.com/modules/oldie-polyfills.js'></script>
            <script src='../code/highcharts.js'></script>
            <script src='../code/modules/exporting.js'></script>
            <script src='../code/modules/export-data.js'></script>
"""


with open('templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
      
    print(file.format('Estadísticas', enHead,"","Estadísticas",
    f"""
    <div class="rectangulo_contenido" id="contenido-grafico-1">
    
    </div>
    <div class="rectangulo_contenido" id="contenido-grafico-2">
    
    </div>
    <div class="rectangulo_contenido" id="contenido-grafico-3">
    
    </div>





<a class="centrar" href="portada.py">Volver al Inicio</a>
        """))