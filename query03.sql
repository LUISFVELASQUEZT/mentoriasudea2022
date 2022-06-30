SELECT sales_manager,
    COUNT (CASE WHEN shipping_address = 'Singapore' THEN order_id END) AS Singapore_Orders,
    COUNT (CASE WHEN shipping_address = 'UK'        THEN order_id END) AS UK_Orders,
    COUNT (CASE WHEN shipping_address = 'Kenya'     THEN order_id END) AS Kenya_Orders,
    COUNT (CASE WHEN shipping_address = 'India'     THEN order_id END) AS India_Orders           
    FROM salesData
    GROUP BY sales_manager