<%@ page import="java.io.PrintWriter" %>
<%@ page import="model.DB" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html; charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>INDEX 2</title>
    <link rel="stylesheet" type="text/css" href="estilos/estilo1.css">
    <script src="js/imagenesVotos.js"> </script>
</head>
<body>
<div class="titulo">INDEX 2</div>

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
        <div class="rectangulo_contenido">

            <% DB  ddbb = new DB("tarea2","root","");
                ResultSet data = ddbb.getAllFotos();

                int i = 1;

                while(data.next()){
                    int mod = i%4;
                    out.println(mod==1);
                    out.println(i==1);

                    String urlImagen = data.getString(2);
                    String nombreOriginalImagen =  data.getString(2);
                    String idImagen =  data.getString(1);
                    if(mod == 1){
                        out.println("<table>");
                    } else if(mod == 0){
                        out.println("</table>");
                    }
                    out.println(
                            " <th >" +
                                    "       <div class='card'> " +
                                    "           <img class= 'center' src= imagenes/"+urlImagen +" alt= "+ nombreOriginalImagen+ " width='120' height='120' >" +
                                    "           <div class='container'>" +
                                    "                <p> iiiii: "+ mod+" </p>"+
                                    "           </div>" +
                                    "       </div>" +
                                    "      </th>");






                    i ++;
                }



            %>




        </div>
    </div>

<div  id = "light_box4" class= "">
    <div class="en-grande ">

    </div>

    <div class="contenido">
        <div class="titulo">
            VOTACION Y COMENTARIO
        </div>
        <div class= "rectangulo_contenido ">
            <div class="caja_form" >
                <form id="votacion" action="vote_handler" method="post">
                    <div >
                        <label>Nota</label>
                        <select name="nota">
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
                        <label>Comentario</label>
                        <input type="text" name="comentario-foto"  cols="50" rows="10" ></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Cometar y Evaluar </button>
                </form>

            </div>

        </div>
    </div>
</div>


</body>
</html>