package model;

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

    public ResultSet getVootes(int id) throws SQLException{
        String query = "SELECT * from comentario_foto WHERE id = ? ";
        //id	fecha	comentario	nota	foto_actividad
        Statement stat = conn.createStatement();
        ResultSet rs = stat.executeQuery(query);
        return  rs;

    }

    public ResultSet getAllFotos() throws SQLException{
        String query = "SELECT * FROM foto";
        Statement stat = conn.createStatement();
        ResultSet rs = stat.executeQuery(query);
        return  rs;
    }

    public void saveVote(String fecha,String comentario,String nota,String foto_actividad) throws SQLException{
        String query = "INSERT INTO comentario_foto (fecha ,comentario ,nota ,foto_actividad) values (?,?,?,?)";
        //id	fecha	comentario	nota	foto_actividad
        try{
            PreparedStatement stat = conn.prepareStatement(query);
            stat.setString(1,fecha);
            stat.setString(2,comentario);
            stat.setString(3,nota);
            stat.setString(4,foto_actividad);
            stat.execute();
        }catch (SQLException e){
            e.printStackTrace();
        }

    }
}

