SELECT product_category, shipping_address, shipping_cost,
        ROW_NUMBER() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC) 
        AS Number,
        RANK() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC)
        AS Rank,
        DENSE_RANK() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC)
        AS DenseRank
        FROM salesData
        WHERE product_category IS NOT NULL 
              AND shipping_address IN ('Germany','India')
              AND status in ('Delivered')   