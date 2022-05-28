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


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Titulo</title>
    
    
</head>
<body >
<div class="titulo">Titulo </div>

<ul class="menu">
  <li class="entrada">
    <a href="portada.py">Home</a>
  </li>
  <li class="entrada">
    <a href="InformarActividad.py">Agregar Actividad</a>
  </li>
  <li class="entrada">
    <a href="listadoActividades.py">Listado Actividades</a>
  </li>
  <li class="entrada">
    <a href="../Estadisticas.py">Estadísticas</a>
  </li>
</ul>
<div class="contenido">
    kkkkkk
</div>
</body>
</html>""")