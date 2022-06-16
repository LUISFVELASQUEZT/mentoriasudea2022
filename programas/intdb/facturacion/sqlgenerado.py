import sqlite3
from sqlite3 import Error

nombreDB="gensql.db"

comandos = []
comandos.append ('''CREATE TABLE `ventas` (
  `id_documento` char(12),
  `id_producto` char(12),
  `fecha` timedate,
  `cantidad` decimal,
  `valor` decimal,
  `costo` decimal,
  PRIMARY KEY (`id_documento`, `id_producto`)
);
''')
comandos.append ('''
CREATE TABLE `facturas` (
  `id_documento` char(12),
  `descripcion` text,
  `fecha` timedate,
  `valor` decimal,
  `nit` char(12),
  PRIMARY KEY (`id_documento`),
  FOREIGN KEY (`id_documento`) REFERENCES `ventas`(`id_documento`)
);
''')
comandos.append('''
CREATE TABLE `clientes` (
  `nit` char(12),
  `nombres` text,
  PRIMARY KEY (`nit`),
  FOREIGN KEY (`nit`) REFERENCES `facturas`(`nit`)
);
''')
comandos.append('''
CREATE TABLE `productos` (
  `id_producto` char(12),
  `descripcion` text,
  PRIMARY KEY (`id_producto`),
  FOREIGN KEY (`id_producto`) REFERENCES `ventas`(`id_producto`)
);
''')

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")
    return conexion

def ejecutar_comando_sql(conexion, comando, msg):
    cursor = conexion.cursor()
    try:
        print(f'{"*" * len(msg)} Inicio de {msg} {"*" * len(msg)}')
        cursor.execute(comando)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")

conexion=crear_conexion(nombreDB)

for comando in comandos:
    ejecutar_comando_sql(conexion, comando, msg=" Creando bd ") 