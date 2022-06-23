package controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.DB;
import org.json.JSONObject;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Fotos extends HttpServlet {

    //Metodo para obtener todas las fotos de la Base de Datos y mostrarlas
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        //id  ruta_archivo  nombre_archivo  actividad_id
        JSONObject jsonR = null;

        try{
            DB ddbb = new DB("tarea2","root","");
            ResultSet rs = ddbb.getAllFotos();
            jsonR = new JSONObject();
            int j = 0;

            while (rs.next()){
                jsonR.put(Integer.toString(j), rs.getInt(3));
                j++;
            }
            String message = jsonR.toString();
            PrintWriter out = response.getWriter();
            out.println(message);
            request.setAttribute("Lista-Fotos",out);
            request.getRequestDispatcher("index.jsp").forward(request,response);
            ddbb.close();

        }catch (SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } catch (ServletException e) {
            throw new RuntimeException(e);
        }


    }

}
