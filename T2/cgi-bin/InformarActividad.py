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



ListaTemas = db.obtener_listado_temas()

opcionestema = ""
for tema in ListaTemas:
    t = tema[0]
    linea  = f"""<option >{tema[0]} </option>""" 
    opcionestema = opcionestema+linea


with open('../templates/template1.html','r', encoding='utf-8') as template:
    file = template.read()
    
    print(file.format('Agregar Actividad', "../estilos/estilo1.css","../FunAct.js","onload='mostrar_regiones(),mostrar_comunas2(),funcion_hora_hoy()'","Agregar Actividad",
    f"""<div>

    <form method="post" action="mensajeFeliz.py" onsubmit="return validar()"   enctype="multipart/form-data">

        <div class="rectangulo_contenido">
            <p class="titulo_chico"> Información del Lugar</p>
            <div>
                <label>Región</label>
                <select name="region"  id="region" >
                    <option disabled selected>Selecciona una región</option>
                </select>
            </div>

            <div>
                <label >Comuna</label>
                <select name="comuna" id = "comuna"  >
                    <option disabled selected>Selecciona una comuna</option>
                </select>
            </div>

            <div>
                <label >Sector </label>
                <input type="text" name="sector" id="sector" size="100">
            </div>
        </div>

        <div class="rectangulo_contenido">
            <p class="titulo_chico"> Datos Organizador</p>
            <div >
                <label >Nombre </label>
                <input type="text" name="nombre" id="nombre" size="100" >
            </div>
            <div>
                <label >Email </label>
                <input type="text" id="email" name="email" size="100">
            </div>

            <div>
                 <label >Número de Celular </label>
                <input type="text" id="celular" name="celular" size="15" placeholder="+56747677707">
            </div>

            <div id="contactar-pors">
                <label> Contartar Por </label>
                <button type="button" onclick="agregar_contactar()">Agregar otra forma de contactar</button>
                <br>
                <div>
                <select  name="contactar-por" >
                    <option disabled selected>Seleccione Forma de  contacto</option>
                    <option >twitter </option>
                    <option >telegram </option>
                    <option >instagram </option>
                    <option >facebook </option>
                    <option >whatsapp </option>
                    <option >tiktok </option>
                    <option >otra </option>
                </select>
                <input type="text" name="contactar-por-link">
                </div>
            </div>
        </div>
        <div class="rectangulo_contenido">
            <p class="titulo_chico"> Cuándo y de qué se trata</p>
            <div>
                <label>Dia Hora Inicio</label>
                <input type="text" name="dia-hora-inicio" >
            </div>

            <div>
                <label>Dia Hora Término</label>
                <input  type="text" name="dia-hora-termino" >

            </div>

            <div>
                <label>Descripción</label>
                <input type="text" name="descripcion-evento" id="descripcion" cols="50" rows="10" ></textarea>
            </div>

            <div id = "box-tema">
                <label>Tema</label>
                <br>
                <div>
                    <select name="tema" onchange="tema_otro()">
                        <option disabled selected>Selecciona un tema</option>
                        <option>Otro </option>
                       


                             {opcionestema}





                        
                    </select>
                    <input class="no_activo" type="text" name="input"  ><br>
                </div>


            </div>

            <div id="box-foto" >
                <label>Foto</label>
                <input type="file" name="foto-actividad">
                <button type="button" onclick="agregar_files()">Agregar otra foto</button>
            </div>
        </div>
        <button type="button" onclick="seguro()">Agregar esta actividad</button>


        <div id="box-confirmacion">
            <p >¿Está seguro que desea agregar esta actividad?</p>
            <input id='botonFormulario' type="submit" value="Sí, estoy seguro">
            <button type="button" onclick="noEnviarFormulario()">No,no estoy seguro, quiero volver al formulario</button>
        </div>



    </form>
</div>""" ))
