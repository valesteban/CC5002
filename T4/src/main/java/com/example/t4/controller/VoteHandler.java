package com.example.t4.controller;
//import org.json.JSONObject;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import com.example.t4.model.DB;
import org.json.JSONObject;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.ResultSet;
import java.sql.SQLException;

public class VoteHandler extends HttpServlet {

    //Metodo que obtiene el votos y comentarios de una foto segun su id
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException{
        JSONObject json = null;
        //comentario_foto
        //id	fecha	comentario	nota	foto_actividad


        int idFoto = Integer.parseInt(request.getParameter("id"));

        try {
            DB ddbb = new DB("tarea2", "root", "");
            ResultSet rs = ddbb.getComentariosNotas(idFoto);
            json = new JSONObject();
            int i = 0;
            while (rs.next()){
                json.put(Integer.toString(i),rs.getInt(4));
                i++;
            }
            String mensaje = json.toString();
            PrintWriter out = response.getWriter();

            out.println(mensaje);
            ddbb.close();
        } catch (SQLException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}