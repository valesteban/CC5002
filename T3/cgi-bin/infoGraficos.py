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

#form = cgi.FieldStorage()

#listaFechas = db.obtenerFechaActividades()


#print("holaaa")

#GRAFICO 1
#el primero es un gráfico de líneas que informa la cantidad de actividades
#por día. En el eje X muestra los días y en el eje Y muestra la cantidad de actividades.




def grafico1():
    
    ActivDia = [0,0,0,0,0,0,0]
    listaFechasActividades = db.obtenerFechaActividades()
    for fecha in listaFechasActividades:
        dia = fecha.weekday()
        ActivDia[dia] += + 1

    return(ActivDia)
#GRAFICO 2
#El segundo gráfico es un gráfico de torta que muestra el total de actividades por tipo
def grafico2():
    listaCantidTemas = db.obtenerAcntidPorActiv()

    dic2 = {}

    nombresTemasId = db.obtenerTemasId()
    for tuplaIdNombre in nombresTemasId:
        dic2[tuplaIdNombre[0]] = tuplaIdNombre[1]
    dic1 = {}
    for tuplaIdCantid in listaCantidTemas:
        dic1[dic2[tuplaIdCantid[0]]] = tuplaIdCantid[1]    
    dicfinal = {}
    for tuplaIdNombre in nombresTemasId:
        if tuplaIdNombre[1] in dic1:
            ##dicfinal[tuplaIdNombre[1]] = dic1[tuplaIdNombre[1]]
            dicfinal[tuplaIdNombre[1]] = dic1[tuplaIdNombre[1]]
        else:
             dicfinal[tuplaIdNombre[1]] = 0       

    return dicfinal

#GRAFICO 3
#El tercer gráfico es uno de barras que muestra tres barras por cada punto del eje X. El eje X son los
#meses y para cada mes muestra una barra con la cantidad de actividades que se inician en la
#mañana (antes de las 11:00), la cantidad de actividades que se inician al mediodía (entre las
#11:00 y 14:59) y la cantidad de actividades que se inician en la tarde (desde las 15:00) . El eje Y
#indica la cantidad.
def grafico3():
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    listaFechasActividades = db.obtenerFechaActividades()
    dic = {}
    for mes in meses:
        dic[mes] = [0,0,0]
    pp = []
    for fecha in listaFechasActividades:
        idmes = fecha.month 
        nombreMes = meses[idmes]
        hora = fecha.hour   
        if hora < 11:
            dic[nombreMes][0] +=1
        elif 11<= hora < 13:
            dic[nombreMes][1] +=1
        else:
            dic[nombreMes][2] +=1

    return dic

info = {"grafico1" :grafico1(),"grafico2" : grafico2(),  "grafico3" : grafico3()}    

print(json.dumps(info))







#print(json.dumps(results))
