<%@ page import="java.io.PrintWriter" %>
<%@ page import="com.example.t4.model.DB" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page import="netscape.javascript.JSObject" %>
<%@ page import="org.json.JSONObject" %>
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
<header><div class="titulo"><h1>INDEX 2</h1></div></header>
<nav>
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
</nav>
<main>
<div class="contenido">
  <div class="rectangulo_contenido">




    <div class="caja_form" >
      <% String idFoto = request.getParameter("id");
        //out.println(idFoto);%>
      <%  DB  ddbb = new DB("tarea2","root","") ;
        ResultSet data = ddbb.getInfoImage(Integer.parseInt(idFoto));
        int idFoto2 = 0;
        String pathFoto = "";
        String nombreRealFoto = "";

        while (data.next()){
          idFoto2 = data.getInt(1);
          pathFoto = data.getString(2);
          nombreRealFoto = data.getString(3);
        }
        out.println("<img class= 'center' src= 'imagenes/"+pathFoto + "' alt='fotito' width='800' height='600'>");

      %>




      <form id="votacion" action="vote_handler" method="post">
        <div >

          <label for="nota" >Nota</label>
          <select id="nota" name="nota">
            <option disabled selected>Selecciona una Nota</option>
            <option value="value1">1</option>
            <option value="value2">2</option>
            <option value="value3">3</option>
            <option value="value3">4</option>
            <option value="value3">5</option>
            <option value="value3">6</option>
            <option value="value3">7</option>
          </select>
        </div>

        <div>
          <label for="comentario-foto" >Comentario</label>
          <input type="text" name="comentario-foto" id="comentario-foto"  cols="50" rows="10" ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Cometar y Evaluar </button>

      </form>
      <div class="notaActual"></div>
      <div id="comentarios" class="comentarios">

        <ul class="listaC">

        </ul>
      </div>

    </div>












  </div>

</div>
</main>

<script src="js/controlVotos.js"></script>
</body>
</html>