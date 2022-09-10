CREATE TABLE "personas" (
  "cedula" char(15), -- 
  "nombres" text,
  "apellidos" text,
  "direccion" text,
  "telefono" text,
  "ciudad" text,
  "email" text, --
  "fecha_re" date,
  PRIMARY KEY ("cedula")
);


CREATE TABLE "prestamos" (
  "cedula" char(15),
  "ejemplar" char(12),
  "fecha_pre" date,
  "fecha_dev" date,
  "id" serial,
  PRIMARY KEY ("id"),
  CONSTRAINT fk_personas
      FOREIGN KEY(cedula) 
	  REFERENCES personas(cedula),
  CONSTRAINT fk_ejemplares
      FOREIGN KEY(ejemplar) 
	  REFERENCES ejemplares(ejemplar)
);

CREATE TABLE "titulos" (
  "isbn" char(12),
  "titulo" text,
  "editorial" text,
  "fecha_pub" date,
  "cantidad" int,
  PRIMARY KEY ("isbn")
);

CREATE TABLE "ejemplares" (
  "ejemplar" char(12),
  "isbn" char(12),
  "fecha-adq" date,
  "costo" decimal,
  "status" boolean,
  PRIMARY KEY ("ejemplar"),
  CONSTRAINT fk_titulos
      FOREIGN KEY(isbn) 
	  REFERENCES titulos(isbn)  
);


CREATE TABLE "autores" (
  "id" serial,
  "nombre" text,
  "apellidos" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "titulo_autor" (
  "isbn" char(12),
  "autor_id" int,
  PRIMARY KEY ("isbn", "autor_id"),
  CONSTRAINT fk_titulos
      FOREIGN KEY(isbn) 
	  REFERENCES titulos(isbn),
 CONSTRAINT fk_autores
      FOREIGN KEY(autor_id) 
	  REFERENCES autores(id) 
  
  
);

CREATE TABLE "titulo_autor" (
  "isbn" char(12),
  "autor_id" int,
  PRIMARY KEY ("isbn", "autor_id"),
  CONSTRAINT fk_titulos
      FOREIGN KEY(isbn) 
	  REFERENCES titulos(isbn),
 CONSTRAINT fk_autores
      FOREIGN KEY(autor_id) 
	  REFERENCES autores(id) 

DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);

CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
   CONSTRAINT fk_customer
      FOREIGN KEY(customer_id) 
	  REFERENCES customers(customer_id)
      
	  
);
