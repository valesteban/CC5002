package com.example.t4.controller;
//import org.json.JSONObject;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import com.example.t4.model.DB;
import org.json.JSONObject;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class VoteHandler extends HttpServlet {

    //Metodo que obtiene el votos y comentarios de una foto segun su id
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException{
        JSONObject json = null;
        //comentario_foto
        //id	fecha	comentario	nota	foto_actividad


        int idFoto = Integer.parseInt(request.getParameter("id"));
        List<Integer> listaNotas = new ArrayList<>();
        List<String> listaComentarios = new ArrayList<>();

        try {
            DB ddbb = new DB("tarea2", "root", "");
            ResultSet rs = ddbb.getComentariosNotas(idFoto);
            json = new JSONObject();
            int i = 0;

            while (rs.next()){
                listaNotas.add(rs.getInt(4));
                listaComentarios.add(rs.getString(3));
               // json.put(Integer.toString(i),rs.getInt(4));
               // i++;
            }
            json.put("notas",listaNotas );
            json.put("comentarios",listaComentarios);

            String mensaje = json.toString();
            PrintWriter out = response.getWriter();

            out.println(mensaje);
            ddbb.close();
        } catch (SQLException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException{
        JSONObject json = null;
        //tabla
        //id	fecha	comentario	nota	foto_actividad

        //parametros post -> idFoto, notaFoto, comentarioFoto, fechaCometarioNota
        int idFoto = Integer.parseInt(request.getParameter("idFoto"));
        int notaFoto = Integer.parseInt(request.getParameter("notaFoto"));
        String comentarioFoto = request.getParameter("comentarioFoto");
        String fechaCometarioNota = request.getParameter("fechaCometarioNota");

      //  Date date = new Date();
       // SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");


        try {
            DB ddbb = new DB("tarea2", "root", "");
            //                  (String fecha,String comentario,int nota,int idFotoActividad)
            ddbb.saveVote(fechaCometarioNota, comentarioFoto, notaFoto, idFoto);
            ddbb.close();
        } catch (SQLException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

    }
}