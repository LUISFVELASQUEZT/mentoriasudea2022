#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

# Ejemplos basados en tutoriales en https://realpython.com/

import sqlite3
from sqlite3 import Error

nombreDB="miBlog.db"

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")
    return conexion

def ejecutar_comando_sql(conexion, comando):
    cursor = conexion.cursor()
    try:
        cursor.execute(comando)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")
        

crear_tabla_de_usuarios = """
CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombres TEXT NOT NULL,
  apellidos TEXT NOT NULL,
  edad INTEGER,
  genero TEXT,
  nacionalidad TEXT,
  ciudad_de_nacimiento TEXT,
  depto_de_nacimiento TEXT
);
"""
crear_tabla_de_publicaciones = """
CREATE TABLE IF NOT EXISTS publicaciones(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  titulo TEXT NOT NULL, 
  descripcion TEXT NOT NULL, 
  fecha DATETIME,
  id_usuario INTEGER NOT NULL, 
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
  
);
"""
crear_tabla_comentarios = """
CREATE TABLE IF NOT EXISTS comentarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  comentario TEXT NOT NULL, 
  fecha datetime,
  id_usuario INTEGER NOT NULL, 
  id_publicacion INTEGER NOT NULL, 
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id) FOREIGN KEY (id_publicacion) REFERENCES publicaciones (id)
);
"""

crear_tabla_me_gusta = """
CREATE TABLE IF NOT EXISTS me_gusta (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  id_usuario INTEGER NOT NULL, 
  id_publicacion integer NOT NULL, 
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id) FOREIGN KEY (id_publicacion) REFERENCES publicaciones (id)
);
"""
agregar_usuarios = """
INSERT INTO
  usuarios (nombres, apellidos, edad, genero, nacionalidad, ciudad_de_nacimiento, depto_de_nacimiento)
VALUES
  ('Carlos','Perez', 25, 'masculino', 'Colombia', 'Envigado', 'Antioquia'),
  ('Lucia', 'Salazar',32, 'femenino', 'Venezuela', 'Maracaibo','Zulia'),
  ('Barbara','Gomez', 35, 'femenino', 'Colombia', 'Usaquen','Cundinamarca'),
  ('Miguel','Cano', 40, 'hombre', 'Chile', 'Santiago','Rm'),
  ('Sofia', 'Leyton', 21, 'femenino', 'Colombia','Tunja','Boyaca'),
  ('Carlos','Ruiz', 32, 'masculino', 'Colombia', 'Medellin', 'Antioquia'),
  ('Lucia', 'Toro',42, 'femenino', 'Colombia', 'Bogota','Cundinamarca'),
  ('Barbara','Ruiz', 45, 'femenino', 'Colombia', 'Usaquen','Cundinamarca'),
  ('Miguel','Urrutia', 50, 'hombre', 'Colombia', 'Bucaramanga','Santander'),
  ('Sofia', 'Gonzalez', 21, 'femenino', 'Colombia','Barranquilla','Atlantico')
  ;
"""
agregar_publicaciones = """
INSERT INTO
  publicaciones (titulo, descripcion, fecha, id_usuario)
VALUES
  ("Entusiasta", "Estoy muy entusiasmado con mi proyecto", "2022-06-13",1),
  ("Como llueve", "Hoy como ayer, está lloviendo mucho en mi pueblo","2022-06-13", 2),
  ("Ofrezco ayuda", "Si necesitas explicaciones de Python, házmelo saber","2022-06-13", 2),
  ("Comienza el 2do ciclo", "Estoy muy entusiasmado con el segundo ciclo que ya comienza", "2022-06-13",1),
  ("Invitacion a unirnos", "Que bueno sería crear un grupo de estudio. Propongo unirnos en Telegram","2022-06-13", 5),
  ("Cooperador", "Puedo ayudar con las herramientas graficas", "2022-06-13",6),
  ("Peticion", "Alguien puede compartirme un buen libro de SQL", "2022-06-13",2),
  ("Formas normales", "Las formas normales de CODD son bien interesantes", "2022-06-13",8),
  ("Como mantener el ritmo", "Alguien conoce una buena técnica de administracion del tiempo","2022-06-13", 8),
  ("Grupo en FB", "O unamos con FB o IG", "2022-06-13", 4),
  ("Grupo en FB", "O unamos con FB o IG ¿Qué les parece?", "2022-06-13",11),  
  ("Diversión", "Programemos un torneo de billar para el inicio del ciclo 2", "2022-06-13",13);
"""

agregar_comentarios = """
INSERT INTO
  comentarios (comentario, fecha, id_usuario, id_publicacion)
VALUES
  ('Me anoto', "2022-06-13", 1, 6),
  ('Cuál tipo de ayuda requieres?', "2022-06-13", 5, 3),
  ('Felicitaciones', "2022-06-13",2, 4),
  ('Me creo un campeón', "2022-06-13", 4, 5),
  ('Te ayudo?', "2022-06-13", 2, 3),
  ('Eres lo máximo',"2022-06-13", 5, 4);
"""

agregar_me_gusta = """
INSERT INTO
  me_gusta (id_usuario, id_publicacion)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""


conexion=crear_conexion(nombreDB)

ejecutar_comando_sql(conexion, crear_tabla_de_usuarios)

ejecutar_comando_sql(conexion, crear_tabla_de_publicaciones) 

ejecutar_comando_sql(conexion,crear_tabla_comentarios)

ejecutar_comando_sql(conexion,crear_tabla_me_gusta)

ejecutar_comando_sql(conexion, agregar_usuarios)

ejecutar_comando_sql(conexion, agregar_publicaciones)

ejecutar_comando_sql(conexion, agregar_comentarios)

ejecutar_comando_sql(conexion, agregar_me_gusta)


