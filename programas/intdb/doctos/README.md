1. ¿Qué es una base de datos? 

Según Wikipedia: 

"En términos generales, una base de datos es un conjunto de datos estructurados que pertenecen a un mismo contexto y, en cuanto a su función, se utiliza para administrar de forma electrónica grandes cantidades de información."

2. ¿Qué es un sistema manejador de bases de datos?

"Hay programas denominados sistemas gestores de bases de datos, abreviado SGBD (del inglés Database Management System o DBMS), que permiten almacenar y posteriormente acceder a los datos de forma rápida y estructurada. Las propiedades de estos DBMS, su utilización y administración se estudian dentro del ámbito de la informática."

3. Aplicaciones comunes

"Las aplicaciones más usuales son para la gestión de empresas e instituciones públicas; también son ampliamente utilizadas en entornos científicos con el objeto de almacenar la información experimental".

4. ¿Qué son las bases de datos relacionales?

Son bases de datos que representan los datos en forma de relaciones según los conceptos establecidos por Codd en el año 1970, en los laboratorios de investigación de IBM en California.

Para definir y manipular una base de datos relacional se usa el lenguage SQL, creado en los años 1970-1980.

5. SQL.

SQL significa lenguaje estructurado de consulta (Structured Query Language).

Consta de dos grandes grupos de instrucciones:

- Lenguaje de definición de datos (DDL)

    Permite definir la estructura de la base de datos

    Ejemplos:

        create database
        create table
        create index
        drop table
        drop index
        drop trigger
        drop view
        create view
        create trigger
        alter table
        create virtual table
        alter index

- Lenguaje de manipulación de datos (DML)

    Permite interactuar con la base de datos

    Ejemplos:

        INSERT  : agrega datos 
        SELECT  : consulta datos
        UPDATE  : modifica datos
        DELETE  : elimina dato   

6. Elementos de una base de datos relacional

- Tabla:  es la unidad básica compuesta de hileras y columnas de datos.
- Índice: son tablas de búsqueda que agilizan el acceso a los datos en una tabla.
- Vista:  es una representación lógica datos de una o de varias tablas 
 
7. Diseño de la base  de datos.

Analicemos este texto, extraído de https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/introduction-to-oracle-database.html#GUID-7BDBD26D-AD11-4599-8C7B-EAB9AAEAA558

7.1. Design for Performance

The key to database and application performance is design, not tuning. While tuning is quite valuable, it cannot make up for poor design. 
Your design must start with an efficient data model, well-defined performance goals and metrics, and a sensible benchmarking strategy.
Otherwise, you will encounter problems during implementation, when no amount of tuning will produce the results that you could have obtained with good design.
You might have to redesign the system later, despite having tuned the original poor design".

7.2 Modelo conceptual.

Mediante análisis se obtiene un  modelo conceptual, plasmado en un diagrama E-R (entidad-relación) en el cual se muestran:

    - las tablas con sus datos.
    - las relaciones entre las tablas.
    - las claves primarias únicas. 

7.3. Modelo lógico    
    
Del diagrama E-R se obtiene el modelo lógico en lenguaje DDL. Algunas herramientas que se emplean para elaborar el diagrama E-R generan el DDL necesario para construír el esquema de la base de datos, pero igualmente se pueden escribir las instrucciones DDL para definir la bd desde un lenguaje como Java o Python. 

Existen varias metodologías y herramientas que ayudan en este proceso.

El diseño de las bases de datos es uno de los factores cruciales en la creación de páginas web dinámicas.

Conocer las relaciones entre los datos y aplicar la normalización hasta la 3NF ayudará grandemente durante el desarrollo del software.

7.4. Formas normales.

En el diseño de las bases de datos relacionales se toma en cuenta la normalización.

Las reglas de Normalización están encaminadas a eliminar redundancias e
inconsistencias de dependencia en el diseño de las tablas

La normalización es un proceso mediante el cual se estructura la base de datos relacional de acuerdo con una serie de reglas llamadas formas normales para reducir la redundancia y mejorar la integridad de los datos.

Esto fue propuesto inicialmente for Edgar F. Codd como parte del modelo relacional.

Ver este ejemplo o abrir los pdf 

 https://lucid.app/lucidchart/2eb05a99-69d2-4051-9dd3-5452236896f4/view?page=0_0&invitationId=inv_ded23cb3-9533-4863-ad47-dfaab79264c3#


 8. Ejercicio de análisis de datos y normalización.

 Analizar el archivo CSV llmado Prueba3NF.csv y generar 
las tablas necesarias para que quede normalizado.

9. INTEGRIDAD REFERENCIAL.

    Permite evitar el que queden datos huérfanos.
    Ver ejemplo de clientes y contactos.

    Al definir las claves foraneas se define si se permite el borrado del registro padre y la acción a seguir en caso de permitirlo:

    DROP TABLE IF EXISTS contactos;
    DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
   cliente_id INT GENERATED ALWAYS AS IDENTIDAD,
   cliente_nombre VARCHAR(255) NOT NULL,
   PRIMARY KEY(cliente_id)
);

CREATE TABLE contactos(
   contacto_id INT GENERATED ALWAYS AS IDENTITY,
   cliente_id INT,
   contacto_nombre VARCHAR(255) NOT NULL,
   telefono VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contacto_id),
   CONSTRAINT fk_cliente
      FOREIGN KEY(cliente_id) 
	  REFERENCES clientes(cliente_id)
	  -- OPCIONES ON DELETE SET NULL
      -- ON DELETE CASCADE
);


Para adicionarle una restricción de claves foráneas a una tabla se puede emplear 

        ALTER TABLE tabla_hija 
        ADD CONSTRAINT nombre_de_la_restriccion 
        FOREIGN KEY (columnas de la llave foránea) 
        REFERENCES tabla_padre (columnas de la tabla padre);

        Ej:

        ALTER TABLE contactos
            ADD CONSTRAINT fk_cliente
            FOREIGN KEY(cliente_id) 
	        REFERENCES clientes(cliente_id)

	        -- OPCIONES ON DELETE SET NULL
            -- ON DELETE CASCADE

10. Concepto de índice

    Permite una búsqueda rápida de registros en una tabla por ampos que no son la clave primaria.

    Ejemplo: buscar libros por título cuando solo se conocen algunas palabras del título:

    - Indices por una sola columna

        CREATE INDEX nombre-indice ON nombre-de-tabla (nombre-columna)

    - Indices de unicidad

        CREATE UNIQUE INDEX nombre-indice ON nombre-tabla (nombre-columna)

    - Indices por varias columnas

       CREATE INDEX nombre-indice ON nombre-de-tabla (nombre-columna, nombre columna, ...)

    - Indices parciales

        CREATE INDEX nombre-indice ON nombre-de-tabla(condicion)

    - Indices implícitos

        Los crea el manejador automáticamente para las claves primarias y campos únicos.

    La definición de índices es un tema muy importante a considerar en el diseño de las bases de datos.


12- CRUD:

    Create >>>>> INSERT
    Read   >>>>> SELECT
    Update >>>>> UPDATE
    Delete >>>>> DELETE 


    Advertencia: Tener mucho cuidado con Update y Delete pues si no se incluye una condición WHERE la operación se aplica a toda la tabla.

13. INSERT INTO tabla (nombre-de-campos-a-insertar) VALUES (lista de valores a insertar);

    En un solo comando se pueden insertar varios registros. Para ello se incluyen varias listas de
    valores , entre paréntesis, separadas por comas y la sentencia termina en ;.

    Hay opciones para insertar en una tabla valores que se hayan consultado mediante un SELECT.

14. SELECT ofrece muchas opciones.

    Desde una sola tabla: SELECT lista-de-campos FROM nombre-de-tabla; la lista puede reemplazarse por  para indicar que se incluyen todos los registros.

    Se pueden seleccionar los que cumplan con alguna condición:

    SELECT campo1, campo2 FROM tabla WHERE condición;

    Ejemplos: 

        SELECT nombre-cliente FROM clientes WHERE nombre-cliente LIKE '%Universidad%' 
                     ORDER BY nombre-cliente;

        SELECT cedula, nombre FROM CLIENTES where saldo > 100000 ORDER BY saldo DESC;

    El estudio de la instrucción SELECT con sus opciones es sumamente importante para sacar el máximo provecho de postgreSQL y de cualquier manejador de bases de datos.

    En el caso de postgreSQL su documentación muestra las siguientes opciones:



        SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]
            [ * | expression [ [ AS ] output_name ] [, ...] ]
            [ FROM from_item [, ...] ]
            [ WHERE condition ]
            [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
            [ HAVING condition ]
            [ WINDOW window_name AS ( window_definition ) [, ...] ]
            [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
            [ ORDER BY expression [ ASC | DESC | USING operator ] [ NULLS { FIRST | LAST } ] [, ...] ]
            [ LIMIT { count | ALL } ]
            [ OFFSET start [ ROW | ROWS ] ]
            [ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
            [ FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE } [ OF table_name [, ...] ] [ NOWAIT | SKIP LOCKED ] [...] ]

    El Manual de postgreSQL es una elemento de trabajo para consultar sobre sintaxis y opciones. Tiene más de 1000 páginas.


    Puede comparar con lo extraído sobre SELECT del manual de MySQL:

    SELECT
        [ALL | DISTINCT | DISTINCTROW ]
        [HIGH_PRIORITY]
        [STRAIGHT_JOIN]
        [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
        [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
        select_expr [, select_expr] ...
        [into_option]
        [FROM table_references
        [PARTITION partition_list]]
        [WHERE where_condition]
        [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
        [HAVING where_condition]
        [WINDOW window_name AS (window_spec)
        [, window_name AS (window_spec)] ...]
        [ORDER BY {col_name | expr | position}
        [ASC | DESC], ... [WITH ROLLUP]]
        [LIMIT {[offset,] row_count | row_count OFFSET offset}]
        [into_option]
        [FOR {UPDATE | SHARE}
        [OF tbl_name [, tbl_name] ...]
        [NOWAIT | SKIP LOCKED]
        | LOCK IN SHARE MODE]
        [into_option]
        into_option: {
        INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        export_options
        | INTO DUMPFILE 'file_name'
        | INTO var_name [, var_name] .


BASE DE DATOS DE PRUEBA

CREACION DE BD DE PRUEBA

Ejecuta psql y responde con la tecla enter a las preguntas correspondientes para que tome los valores por defecto

    Server [localhost]:
    Database [postgres]:
    Port[5432]:
    Username [postgres]:

Recibirás algunos mensajes y finalmente el prompt que indica que estás conectado como postgres;

postgres=#

Para ver las bases de datos que tienes introduce el comando siguiente:

\l

Recibirás como respuesta los nombres de tres bases de datos que se instan en postgres automáticamente: postgres, template0 y template1

Ahora crearemos una base de datos con la instrucción SQL correspondiente:

CREATE DATABASE biblio;

Das enter después del ";" y después de unos segundos recibirás el mensaje CREATE DATABASE

Nota: las instrucciones de SQL se pueden escribir en mayúsculas o en minúsculas. Para resaltarlas se escribirán en mayúscula en este documento. Los términos en minúscula son los que deberás suministrar al comando. En este caso de CREATE DATABASE biblio es el nombre de la base de datos.

Confirma ahora que la base de datos está creada con el comando \l

Nota: Si has dividido tu pantalla con símbolo de Windows flecha izquierda o derecha para tener al mismo tiempo la ventana de psql y este documento, entonces puedes ingresar el comando \x a psql para que la visualización de datos sea verticalmente y facilite la lectura. \x es un switch. Es decir, si vuelves a ingresar el comando \x cambio al despliegue horizontal.

CREACION DE TABLAS.

En este momento biblio no tiene definida ninguna tabla. Vamos a definirle 4 tablas según el 
modelo visto en el modelado de datos:

    tabla persona
    tabla titulo
    tabla autor
    tabla prestamos
    tabla ejemplar
    tabla titulo-autor

TABLA PERSONA: contendrá un registro por cada persona que se afilia a la biblioteca. La clave primaria es la cédula.

La instrucción para crearla es la siguiente:

CREATE TABLE IF NOT EXISTS persona
  (cedula VARCHAR(20) PRIMARY KEY NOT NULL,
   nombre VARCHAR(50) NOT NULL,
   apelllido VARCHAR(50) NOT NULL,
   genero VARCHAR(10) NOT NULL);


Puedes ejectar el comando ingresando línea por línea, terminando la última con ';'. Eso indica a psql el final del comando y lo valida y ejecuta. Si todo está bien, verás la respuesta CREATE TABLE. De 
lo contrario te marcará los errores.

Para verificar que la tabla fue creada usa el comando \dt y te mostrará el esquema, el nombre, tipo y dueño.

El comando \d persona te mostrará la definición de la tabla persona, una línea por cada campo con su tipo y muestra en la parte inferior los índices que haya.
En este caso "persona_pkey" PRIMARY KEY, btree (cedula)

AGREGAR DATOS

Ejecutamos la inserción con la instrucción SQL INSERT. Corresponde a la letra "C" del CRUD.

Primero comprueba que la tabla persona no contiene datos con la instrucción siguiente:

SELECT * FROM persona;

Recuera terminar con ";"

Ahora inserta el dato que desees:

INSERT INTO persona(cedula, nombre, apellido, genero) 
       VALUES ('1212312345','Pedro','Perez','Masculino'),
              ('2424624690','Juan','Galindo','Masculino');

Puedes insertar varios registros indicando la lista de valores de cada uno entre paréntesis, separando las        listas por comas y dando el ; al final. 

Si intentas ejecutar este comando dos veces,  con los mismos datos , vas a recibir una respuesta con un rechazo por el control que se hace por la llave primaria.

AGREGAR UN CAMPO A LA TABLA

Si agregamos el correo lo hacemos con 

ALTER TABLE persona ADD COLUMN email VARCHAR(30);

Ahora actualicemos los correos de las dos personas:

ALTER TABLE persona RENAME COLUMN email TO correo;

Podemos probar con el uso de funciones. 
Supongamos que los dos tienen el correo nombre.apellido@gmail.com

Ejecuta la siguiente instrucción de actualizacón (Update) y sería la U del  CRUD.

UPDATE persona SET correo = CONCAT(nombre, '.', apellido ,'@gmail.com') ;

postgreSQL ofrece una gran variedad de funciones. Para ver el detalle puedes consultar el manual de postgreSQL en 

https://www.postgresql.org/files/documentation/pdf/14/postgresql-14-US.pdf

Este manual de la versión tiene  3002 páginas Een formato carta. Puedes descargarlo y tenerlo a tu disposición o consultarlo en línea.

Cambia ahora la definición de la tabla persona para hacer requerido el campo correo. Para ello ingresa la siguiente instrucción:

ALTER TABLE persona ALTER COLUMN correo SET NOT NULL;

Puedes agregar a tu gusto registros a la tabla persona.

Ahora vamos a agregarle a 
la tabla personas dos campos:

- ciudad
- fecha de nacimiento

ALTER TABLE persona ADD COLUMN ciudad VARCHAR(20) NOT NULL;

ALTER TABLE persona ADD COLUMN fecha_de_nacimiento DATE;


Vamos a actualizar los datos de los registros con las siguientes instrucciones:

UPDATE persona SET ciudad = 'Envigado', fecha_de_nacimiento = DATE '1990-01-01' WHERE nombre ILIKE '%pedro%';

Incluimos en estas dos instrucciones el uso de la función DATE. Puedes estudiarla en el manual de postgreSQL. Es una función muy útil que tiene mucha aplicación.

Igualmente usamos la función ILIKE  para buscar expresiones regulares como '%pedro%' indicando que busque los registros que en el nombre contengan 'pedro' escrito con mayúscula o minúscula o combinación. Las expresiones regulares permiten armar búsquedas muy completas y complejas.

Ahora modificaremos la definición de la tabla para que tanto la ciudad como la fecha sean requeridas.

ALTER TABLE persona ALTER COLUMN ciudad SET NOT NULL;
ALTER TABLE persona ALTER COLUMAN fecha_de_nacimiento SET NOT NULL;

De aquí en adelante al registrar una persona se exigirán la fecha de nacimiento y la ciudad.

SELECT GROUP BY ORDER BY

Para consultar todos los registros:

SELECT nombre, apellido, ciudad FROM persona ORDER BY ciudad;

Prueba esta opción de agrupamiento y conteo:

SELECT  ciudad, COUNT(*) FROM persona GROUP BY ciudad ORDER  ciudad;


Ahora prueba esta opción y saca tus conclusiones:

SELECT  ciudad, COUNT(*) FROM persona
         GROUP BY ciudad
         HAVING COUNT(*) > 1 ORDER BY ciudad;


FUNCION AGE:

Prueba los siguientes dos comandos y saca tus conclusiones.

SELECT  nombre, apellido, correo, fecha_de_nacimiento, EXTRACT (YEAR FROM AGE(fecha_de_nacimiento))  FROM persona;

SELECT  nombre, apellido, fecha_de_nacimiento, AGE(fecha_de_nacimiento)  FROM persona;

VISTAS - VIEWS

CREATE VIEW vista AS
	SELECT dato1, dato2, dato3, dato5, dato6, dato7
	FROM tabla1, tabla2
	WHERE tabla1.dato = tabla2.dato;

Uso:

SELECT * FROM vista;

EJEMPLOS DE PUNTOS DE RECUPERACIÓN - COMMIT - ROLLBACK

BEGIN;
UPDATE cuenta_ahorros SET balance = balance - 100.00
WHERE nombre = 'Luis';
SAVEPOINT punto1;
UPDATE cuenta_ahorros SET balance = balance + 100.00
WHERE nombre = 'Juan';
-- error... se empleó una cuenta que  no era
ROLLBACK TO punto1;
UPDATE cuenta_ahorros SET balance = balance + 100.00
WHERE nombre = 'Pedro';
COMMIT;


La ciudad debe ser una de las siguientes: Medellin, Envigado,Bogota, Sincelejo, Cali, Barranquilla. La lista podría ser mayor, solo se colocan estas para probar.

NOTAS TOMADAS DEL MANUAL DE POSTGRES 14.5

