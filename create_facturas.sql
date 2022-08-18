CREATE TABLE IF NOT EXISTS facturas(
  tipo_documento CHAR(3) NOT NULL,
  id_documento CHAR(12) NOT NULL,
  descripcion TEXT NOT NULL,
  fecha timedate,
  valor DECIMAL, 
  rut,
  PRIMARY KEY (tipo_documento, id_documento),
  FOREIGN KEY (rut) REFERENCES clientes (rut)
  );