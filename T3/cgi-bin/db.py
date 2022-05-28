#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
import sys
import cgitb
import cgi
cgitb.enable()
class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def guardar_nuevo_tema(self,data):
        """
        Este metodo se le pasa el nombre del nuevo tema y lo guarda en la base de datos en la tabla
        tema
        """ 
        sql = f''' 
           INSERT INTO `tema`( `nombre`) VALUES ('{data}')
            '''
        
        self.cursor.execute(sql)
        self.db.commit()  

    def obtenerIdTema(self,data):  
        """
        Metodo que recibe el nombre del tema, lo busca el la tabla tema y devuleve su id
        """
        sql = f'''
        SELECT id FROM tema Where nombre= "{data}"
        '''
        #print("la buequeda es: ",sql)
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()




    def guardar_actividad(self, data):
        """ 
        Este método guarda una actividad en la base de datos.
        """
#

        # Guardar Actividad

        #obtenemos el id del tema si es otro tenemos que agregar este tema a la tabla tema
        #(130204, 'hnbgf', 'valentina', 'vale@gmail.cl', '+56950102497', '2022-05-02 15:56', '2022-05-02 18:56', 'holahola', ['Política'], ['otrotemainput'])
        #print(data)

        #si el tema es "Otro" lo guardo en la base de datos y agrego su id 
        tema = data[8][0]
        if(tema =="Otro"):
            #print("guardamos el nuevo tema")
            tema = data[9][0]
            self.guardar_nuevo_tema(tema)

        #Buscamos el id del tema
        #t= self.obtenerIdTema(tema)
        #print(t)
        #print(tema[:15])
        id_tema = self.obtenerIdTema(tema[:15])[0][0]   #[(17,)]

        #AHORA GUARDAMOS LA ACTIVIDAD
        sql = '''
            INSERT INTO actividad (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id)
            VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)
            '''
        tupla =  data[:7]+ (tema,) +(id_tema,)
        #data = (data[:7]+ tema)

        self.cursor.execute(sql, tupla)  # ejecuta la consulta
        self.db.commit()                # modifico la base de datos

    def guardar_fotos(self,data):
        """
        Metodo que resive una fileStograge con la imagen o unna lita con varias FielStoge de imagenes.
        Esta revisara y las guardara en la base de datos ademas de que se guardaran las imagen en el servidor
        """
        #OBTENER EL ID DE LA ACTIVIDAD
        sql_id = ''' SELECT MAX(ID) FROM actividad'''
        self.cursor.execute(sql_id)  # ejecuta la consulta
        id_actividad = self.cursor.fetchall()[0][0]  #[(1,)]
        #print(id_actividad)
        if(type(data) is not list):
            data =  [data]

        #data = #[MiniFieldStorage('foto', 'tarea2.png'), MiniFieldStorage('foto', 'tarea2.png')]
        
        for fs in data:
            #self.cursor.execute(sql_file, (filename, filename_hash))  # ejecuta la query que guarda el archivo en base de datos
            
            filename = fs.filename

            sql = "SELECT COUNT(id) FROM foto" # Cuenta los archivos que hay en la base de datos
            self.cursor.execute(sql)
            total = self.cursor.fetchall()[0][0] + 1
            filename_hash_path = hashlib.sha256(filename.encode()).hexdigest()[0:30] # aplica función de hash
            filename_hash_path += f"_{total}" # concatena la función de hash con el número total de archivos, nombre único
        
            # Guardar archivo
            #try:
            open(f"imagenes/{filename_hash_path}", "wb").write(fs.file.read()) # guarda el archivo localmente
            sql_file = '''
                INSERT INTO foto (ruta_archivo,nombre_archivo,actividad_id) 
                VALUES (%s, %s,%s)
                '''

            tupla =  (filename_hash_path, filename)+(id_actividad,)
            

            self.cursor.execute(sql_file, (filename_hash_path, filename)+(id_actividad,))  # ejecuta la query que guarda el archivo en base de datos
            self.db.commit()   


        
    def guardar_contactos(self,data):
        """
        Metodo que recive lista de tuplas con la forma de contactar y el 'usuario' o algo asi
        Para guardarlas en la base d e datos
        """
        #[('twiter', 'twtwtwite'), ('Telegram', 'tetet')]

        #ID DE LA ACTIVIDAD
        sql_id = ''' SELECT MAX(ID) FROM actividad'''
        self.cursor.execute(sql_id)  # ejecuta la consulta
        id_actividad = self.cursor.fetchall()[0][0]  #[(1,)]
        

        for tupla in data:
            nombre = tupla[0]  #twitter,telegram y esas cosas
            identificador = tupla[1]
            sql = '''
                INSERT INTO contactar_por (nombre, identificador, actividad_id) 
                VALUES (%s,%s,%s)'''

            tupla = (nombre,identificador,id_actividad) 
            

            self.cursor.execute(sql, tupla )  # ejecuta la query que guarda el archivo en base de datos
            self.db.commit()      




    def obtenerComunaIdRegioId(self,data):
        """ 
        Este método obtiene el id de la comuna y de la region a la que pertenece.
        """
        
        sql = f'''
        SELECT id, region_id  FROM comuna WHERE nombre = "{data}"
        '''
        self.cursor.execute(sql)  # ejecuta la consulta
     
        return  self.cursor.fetchall()
        


    def obtener_ultimas5_actividades(self):
        """
        Metodo que retorna las ultimas 5 actividades agregadas en la base de datos
        """
        sql = '''
            SELECT AC.id, CO.nombre, AC.sector, AC.nombre, AC.email, AC.celular, AC.dia_hora_inicio, AC.dia_hora_termino, AC.descripcion, TE.nombre FROM actividad AC, comuna CO, tema TE WHERE AC.comuna_id=CO.id AND AC.tema_id=TE.id ORDER BY id DESC LIMIT 5
            '''

        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()

    def obtener_imagen_por_id(self,data) :
        """
        Metodo que recibe un id de la actividad y retrona todas sus imagenes de la base de datos
        """
        sql = f'''
        SELECT * FROM foto WHERE actividad_id = {data}'''
        #print(sql)  

        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()

    def obtener_listado_temas(self):    
        """
        Metodo que retorna lista de tuplas con los temas dentro de la base de datos
        [('música',), ('deporte',), ('ciencias',) ]
        """

        sql = '''
            SELECT nombre FROM tema WHERE 1
            '''
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()
    
    def obtener_todas_actividades(self):
        """
        Metodo que retorna todas las actividades de la base de datos
        [(2, 130210, 'Beauchef 850, terraza', 'Matías Cordón', 'MatiasCordon@gmail.com', '+569111024977', datetime.datetime(2022, 3, 23, 12, 0), datetime.datetime(2022, 5, 23, 14, 0), '"""

        sql = '''
            SELECT id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tema_id FROM actividad
            '''
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()   

    def obtener_comuna_por_id(self,data):
        """
        Metodo que recibe el id de una comuna y devuelve el nombre de la comuna
        de la forma [('Maule',)]
        """     

        sql = f"""
                SELECT * FROM comuna WHERE id ={data} """

        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()  

    def obtener_actividad_por_id(self,data):
        """
        Metodo que recibe un int y bsca la actividad segun su id en la basede datos.
        Devuelve una lista con la tupla qu ecorresponde 
        [(2, 130210, 'Beauchef 850, terraza', 'Matías Cordón', 'MatiasCordon@gmail.com', '+569111024977', datetime.datetime(2022, 3, 23, 12, 0), datetime.datetime(2022, 5, 23, 14, 0), 'Escuela de Boxeo', 56)]
        """

        sql =f'''
            SELECT * FROM actividad WHERE id={data}
            '''             
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()      

    def obtener_region_por_id(self,data):
        """
        Metodo que recibe int corrspondiente al id de la region y devuelve toda la info de la region
        """

        sql = f'''SELECT * FROM region WHERE id ={data} '''
        
        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall() 

    def obtener_contacto_por_actividad_id(self,data):
        """
        Metodo que reicbe id de la actividad y la busca en la tabla de contactos y devuelvo todos los contatos 
        [(7, 'twitter', 'MatíasCordóntwitter', 2), (8, 'telegram', 'MatíasCordóntelegram', 2)]"""

        sql = f'''
            SELECT * FROM contactar_por WHERE actividad_id ={data}''' 

        self.cursor.execute(sql)  # ejecuta la consulta
        return  self.cursor.fetchall()         