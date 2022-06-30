import sqlite3 as sq
myDB = "learning.db"
try:
    sqConexion = sq.connect(myDB)
    cursor=sqConexion.cursor()
    print(f'Conexion exitosa a {myDB}')
    sqQuery = "select sqlite_version()"
    cursor.execute(sqQuery)
    datos = cursor.fetchall()
    print(f' Version de SQLITE es {datos}')
    
    sq_crear_tabla = '''CREATE TABLE learningdb_personas (
                                cedula INTEGER PRIMARY KEY,
                                nombre TEXT NOT NULL,
                                apellidos TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                fecha_contrato datetime,
                                celular TEXT NOT NULL,
                                direccion TEXT,
                                ciudad TEXT,
                                genero TEXT
                                salario REAL NOT NULL);'''

    cursor.execute(sq_crear_tabla)
    sqConexion.commit()
    print("SQLite table created")

    cursor.close()
    
except sq.Error as e:
    print(f' Ocurrió el error {e} al conectarse a {myDB}')
finally:
    if sqConexion:
        sqConexion.close()
        print(f'Conexion a {myDB} se cierra!')