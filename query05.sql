SELECT order_id, order_date, quantity,
    CASE    WHEN quantity > '60' THEN 'High'
            WHEN quantity < 51 THEN 'Low'
            
    END AS  OrderVolume
    FROM salesData