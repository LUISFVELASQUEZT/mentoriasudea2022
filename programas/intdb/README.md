¿Qué es una base de datos? 

Según Wikipedia: 

"En términos generales, una base de datos es un conjunto de datos estructurados que pertenecen a un mismo contexto y, en cuanto a su función, se utiliza para administrar de forma electrónica grandes cantidades de información.1"

¿Qué es un sistema manejador de bases de datos?

"Hay programas denominados sistemas gestores de bases de datos, abreviado SGBD (del inglés Database Management System o DBMS), que permiten almacenar y posteriormente acceder a los datos de forma rápida y estructurada. Las propiedades de estos DBMS, así como su utilización y administración, se estudian dentro del ámbito de la informática."

Aplicaciones comunes

"Las aplicaciones más usuales son para la gestión de empresas e instituciones públicas; también son ampliamente utilizadas en entornos científicos con el objeto de almacenar la información experimental".

¿Qué son las bases de datos relacionales?

Son bases de datos que representan los datos en forma de relaciones según los conceptos establecidos por Codd en el año 1970, en los laboratorios de investigación de IBM en California.

Para definir y manipular una base de datos relacional se usa el lenguage SQL, creado en los años 1970-1980.

SQL significa lenguaje estructurado de consulta (Strucutured Query Language).

Tiene dos grandes grupos de instrucciones:

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

Componentes de la base de datos relacional

- Tabla:  es la unidad básica compuesta de hileras y columnas de datos.
- Índice: son tablas de búsqueda que agilizan el acceso a los datos en una tabla.
- Vista:  es una representación lógica datos de una o de varias tablas 
 
Diseño de la base  de datos.

Es el proceso que se lleva a cabo para obtener el diseño de la base de datos.
En un proceso de análisis se obtiene un diseño con un  modelo conceptual, plasmdo en un diagrama llamado E-R (entidad-relación) en el cual se muestran:

    - las tablas con sus datos.
    - las relaciones entre las tablas.
    - las claves primarias únicas.     
    
Del diagrama E-R pasamosg al modelo lógico en lenguaje DDL. Algunas herramientas que se emplean para elaborar el diagrama E-R generan el DDL necesario para construír el esquema de la base de datos.

Existen varias metodologías y herramientas que ayudan en este proceso.

En el diseño de las bases de datos relacionales se toma en cuenta la normalización.

https://en.wikipedia.org/wiki/Database_normalization#Initial_data

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity. It was first proposed by Edgar F. Codd as part of his relational model.

Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. It is accomplished by applying some formal rules either by a process of synthesis (creating a new database design) or decomposition (improving an existing database design).

Satisfying 1NF
To satisfy First normal form, each column of a table must have a single value. Columns which contain sets of values or nested records are not allowed.

In the initial table, Subject contains a set of subject values, meaning it does not comply.

To solve the problem, the subjects are extracted into a separate Subject table:[10]

Satisfying 1NF
To satisfy First normal form, each column of a table must have a single value. Columns which contain sets of values or nested records are not allowed.

In the initial table, Subject contains a set of subject values, meaning it does not comply.

To solve the problem, the subjects are extracted into a separate Subject table:[10]

A foreign key column is added to the Subject-table, which refers to the primary key of the row from which the subject was extracted. The same information is therefore represented but without the use of non-simple domains.

Instead of one table in unnormalized form, there are now two tables conforming to the 1NF.


Satisfying 2NF
If a table has a single column primary key, it automatically satisfies 2NF, but if a table has a multi-column or composite key then it may not satisfy 2NF.
The Book table below has a composite key of {Title, Format} (indicated by the underlining), so it may not satisfy 2NF. At this point in our design the key is not finalised as the primary key, so it is called a candidate key. Consider the following table:

All of the attributes that are not part of the candidate key depend on Title, but only Price also depends on Format. To conform to 2NF and remove duplicities, every non candidate-key attribute must depend on the whole candidate key, not just part of it.

To normalize this table, make {Title} a (simple) candidate key (the primary key) so that every non candidate-key attribute depends on the whole candidate key, and remove Price into a separate table so that its dependency on Format can be preserved:

Now, the Book table conforms to 2NF.

Satisfying 3NF
The Book table still has a transitive functional dependency ({Author Nationality} is dependent on {Author}, which is dependent on {Title}). A similar violation exists for genre ({Genre Name} is dependent on {Genre ID}, which is dependent on {Title}). Hence, the Book table is not in 3NF. To make it in 3NF, let's use the following table structure, thereby eliminating the transitive functional dependencies by placing {Author Nationality} and {Genre Name} in their own respective tables:
