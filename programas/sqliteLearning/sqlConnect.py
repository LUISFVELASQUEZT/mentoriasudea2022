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
    cursor.close()
except sq.Error as e:
    print(f' Ocurrió el error {e} al conectarse a {myDB}')
finally:
    if sqConexion:
        sqConexion.close()
        print(f'Conexion a {myDB} se cierra!')