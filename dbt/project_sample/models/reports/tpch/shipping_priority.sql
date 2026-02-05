-- TPC-H/TPC-R Shipping Priority Query (Q3)
SELECT
    l.order_id,
    o.order_date,
    o.ship_priority,
    SUM(l.extended_price * (1 - l.discount)) AS revenue
FROM
    {{ ref('stg_tpch__customer') }} AS c
INNER JOIN {{ ref('stg_tpch__orders') }} AS o ON c.customer_id = o.customer_id
INNER JOIN {{ ref('stg_tpch__lineitem') }} AS l ON o.order_id = l.order_id
WHERE 1 = 1
GROUP BY
    l.order_id,
    o.order_date,
    o.ship_priority
