# !/usr/bin/python3
# -*- coding: utf-8 -*-

from cmath import inf
from multiprocessing.dummy import active_children
import sys
import cgi
import json
from db import DB
import datetime


print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'tarea2')

#como todas las actividades si o si tendran imagenes 
listita = db.obtenerIdCOmunasActividades()

listitaComunas = []
for id in listita:
    comunaNombre = db.obtener_comuna_por_id(id)
    listitaComunas.append(comunaNombre[0][1])

with open('../chileComunas.json') as file:
    data = json.load(file)
dic = {}
for valores in data:
    vv = valores["name"]
    if vv in listitaComunas:
        dic[vv] = (valores["lng"],valores["lat"])
        
    
#dicc tiene las cominas con sus lat y log


print(json.dumps(dic))