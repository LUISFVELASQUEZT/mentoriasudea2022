WITH SM AS MATERIALIZED
     (SELECT DISTINCT sales_manager FROM salesData
          WHERE shipping_address = 'Germany' and unit_price > 150.0
    ), PC AS MATERIALIZED
    
    (SELECT DISTINCT product_category FROM salesData
            WHERE product_category = 'Healthcare' AND unit_price > 150.0
    
    )
    
    SELECT sales_manager,
        product_category,
        unit_price
        FROM salesData
        WHERE product_category IN (
            SELECT product_category FROM PC)
        AND sales_manager IN (
                SELECT sales_manager FROM SM
            )
        AND unit_price > 150.0
    ORDER BY unit_price DESC