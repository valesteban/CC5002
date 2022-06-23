package controller;
//import org.json.JSONObject;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import model.DB;
import org.json.JSONObject;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.ResultSet;
import java.sql.SQLException;

public class VoteHandler extends HttpServlet {

    //Metodo que obtiene el votos y comentarios de una foto segun su id
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException{
        JSONObject json = null;

        try{
            DB ddbb = new DB("tarea2","root","");
            ResultSet rs = ddbb.getVootes(Integer.parseInt(request.getParameter("id_foto")));
            json = new JSONObject();
            int i = 0;

            while (rs.next()){
                json.put(Integer.toString(i), rs.getInt(3));
                i++;
            }
            String message = json.toString();
            PrintWriter out = response.getWriter();
            out.println(message);
            ddbb.close();

        }catch (SQLException | ClassNotFoundException e){
            e.printStackTrace();
        }


    }
    //Metodo que guardará en la base de datos la nota y comentario de la foto
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException{
        String id = request.getParameter("");
    }
}
