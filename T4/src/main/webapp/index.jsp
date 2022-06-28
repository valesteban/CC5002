<%@ page import="java.io.PrintWriter" %>
<%@ page import="com.example.t4.model.DB" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html; charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>INDEX 2</title>
    <link rel="stylesheet" type="text/css" href="estilos/estilo1.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="js/imagenesVotos.js"> </script>
</head>
<body>
<div class="titulo"><h1>INDEX 2</h1></div>

<ul class="menu">
    <li class="entrada">
        <a href="">Home</a>
    </li>
    <li class="entrada">
        <a href="">Agregar Actividad</a>
    </li>
    <li class="entrada">
        <a href="">Listado Actividades</a>
    </li>
    <li class="entrada">
        <a href="">Estadísticas</a>
    </li>
</ul>
    <div class="contenido">
        <div id="tablaFotos" class="rectangulo_contenido">

        //    <% DB  ddbb = new DB("tarea2","root","");
                ResultSet data = ddbb.getAllFotos();

                int i = 1;

                while(data.next()){
                    int mod = i%4;

                    String urlImagen = data.getString(2);
                    String nombreOriginalImagen =  data.getString(2);
                    String idImagen =  data.getString(1);
                    String funcion = "redirigir("+idImagen+")";
                    if(mod == 1){
                        out.println("<table>");
                    }
                    out.println(
                            " <th onclick='"+funcion+"'>" +
                            "           <img class= 'center' src= imagenes/"+urlImagen +" alt='imagen'  width='200' height='120' ></img>" +
                            " </th>");
                    if(mod == 0){
                        out.println("</table>");
                    }





                    i ++;
                }



            %>

        </div>

    </div>











</body>
</html>