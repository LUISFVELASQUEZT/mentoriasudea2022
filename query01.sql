select facturas.nit, nombres, 
       substr(facturas.descripcion,1,3) as TD,
	   facturas.id_documento as Docto,
	   facturas.fecha,
	   ventas.id_producto,
	   productos.descripcion,
	   cantidad
	   from facturas
	   inner join clientes
	   on facturas.nit = clientes.nit
       inner join ventas
	   on facturas.id_documento = ventas.id_documento
	   inner join productos
	   on ventas.id_producto = productos.id_producto
	   ORDER BY nombres, facturas.id_documento
	   