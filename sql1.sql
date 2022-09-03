select nit, nombres, facturas.ID_documento, 
    id_producto, productos.descripcion, facturas.fecha, 
	substr(facturas.fecha,7,4) as AÑO,
	case when substr(facturas.fecha,4, 2) in ("01","02","03","04","05","06") 
			THEN 01 ELSE 02 END SEM,
	cantidad, cantidad * ventas.valor as Monto, cantidad * ventas.costo as Costo
	from clientes 	join facturas using (nit) 
	join ventas using (id_documento) 
	join productos using (id_producto)
	order by nit