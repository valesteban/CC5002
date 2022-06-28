package com.example.t4.model;

import java.io.PrintWriter;
import java.sql.*;

public class DB {
    private Connection conn;

    public DB(String db,String user, String pass) throws ClassNotFoundException, SQLException{
        Class.forName("com.mysql.cj.jdbc.Driver");
        this.conn = DriverManager.getConnection("jdbc:mysql://localhost/"+ db + "?user="+ user + "&password=" + pass);

    }

    public void close() throws SQLException{
        this.conn.close();
    }

    public ResultSet getComentariosNotas(int id) throws SQLException {
        //id	fecha	comentario	nota	foto_actividad
        String query = "SELECT * from comentario_foto WHERE foto_actividad = ? ORDER BY fecha DESC ";
        PreparedStatement stat = conn.prepareStatement(query);
        stat.setInt(1,id);
        ResultSet rs = stat.executeQuery();
        return rs;
    }

    public ResultSet getAllFotos() throws SQLException{
        String query = "SELECT * FROM foto";
        Statement stat = conn.createStatement();
        ResultSet rs = stat.executeQuery(query);
        return  rs;
    }
    public ResultSet getInfoImage(int id) throws SQLException{
        String query = "SELECT * FROM foto WHERE id = ?";

        PreparedStatement stat = conn.prepareStatement(query);
        stat.setInt(1,id);
        ResultSet rs = stat.executeQuery();
        return rs;
    }


    public void saveVote(String fecha,String comentario,int nota,int idFotoActividad) throws SQLException{
        String query = "INSERT INTO comentario_foto (fecha ,comentario ,nota ,foto_actividad) values (?,?,?,?)";
        //id	fecha	comentario	nota	foto_actividad
        //en foto actividad de la tabla comentario_foto va  air el id de la foto de la tabla foto
        try{
            PreparedStatement stat = conn.prepareStatement(query);
            stat.setString(1,fecha);
            stat.setString(2,comentario);
            stat.setInt(3,nota);
            stat.setInt(4,idFotoActividad);
            stat.execute();
        }catch (SQLException e){
            e.printStackTrace();
        }

    }
}

