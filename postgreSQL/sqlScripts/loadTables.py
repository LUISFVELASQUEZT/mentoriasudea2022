from optparse import Values


insert into "personas" (
  "cedula" , -- char(15)
  "nombres", -- text
  "apellidos", -- text,
  "direccion", -- text,
  "telefono", -- text,
  "ciudad", -- text,
  "email", -- text,
  "fecha_re" -- date,
  ) Values
('1','Luis','Rodriguez','Calle 20', '312-3143154','Envigado','email@gmail.com','01-09-2022'),
('111','Luis','Ochoa','Calle 40', '312-3143155','Envigado','email@gmail.com','01-09-2022'),
('11111','Luis','Gonzalez','Calle 55', '312-3143165','Envigado','email@gmail.com','01-09-2022'),
('22222','Luis','Velasquez','Calle 60', '312-3143167','Envigado','email@gmail.com','01-09-2022');

insert into "titulos" (
  "isbn" , -- char(12) PK
  "titulo", -- text,
  "editorial", -- text,
  "fecha_pub", -- date,
  "cantidad") -- int)
VALUES 
('3-528-6654-0','Java 9 for Programmers','Pearson','01-01-2018',2),
('8129-7891-9','Portraits and Observations','Random House','01-01-1993',1),
('3-528-9954-0','Advanced Java for Programmers','Pearson','01-01-2018',3),
('9929-7891-9','Musica para camaleones','Random House','01-01-1993',2);

insert into "ejemplares" (
  "ejemplar",  --char(12),PRIMARY KEY ("ejemplar"),
  "isbn",  --char(12), REFERENCES titulos(isbn)
  "fecha-adq",  --date,
  "costo", --decimal,
  "status")  
Values
    ('EJ1111','3-528-6654-0','01-09-2021',11800,True),
    ('EJ2','3-528-6654-0','01-09-2021',11800,True),
    ('EJ11','8129-7891-9','01-09-2021',11800,True),
    ('EJ111','9929-7891-9','01-09-2021',11800,True);
    
insert into "prestamos" (
  "cedula" , -- char(15), FOREIGN KEY(cedula) REFERENCES personas(cedula),
  "ejemplar", -- char(12), FOREIGN KEY(ejemplar) REFERENCES ejemplares(ejemplar)
  "fecha_pre" , -- date,
  "fecha_dev") --  date
  
values('1', 'EJ1111', '01-09-2022', '01-10-2022'),
      ('111','EJ2', '01-09-2022', '01-10-2022'),
      ('1', 'EJ2', '01-09-2022', '01-10-2022'),
      ('1', 'EJ1111', '01-09-2022', '01-10-2022');
      
insert into "autores" (
  "nombre", "apellidos" ) Values
   ('Truman','Capote'),
   ('Alvaro','Mutis'),
   ('Deitel','Deitel')
;
      
    
    
    
  
  












