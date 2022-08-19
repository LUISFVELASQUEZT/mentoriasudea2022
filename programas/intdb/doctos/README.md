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
        alter table
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

