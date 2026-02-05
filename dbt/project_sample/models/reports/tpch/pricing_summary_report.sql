-- TPC-H/TPC-R Pricing Summary Report Query (Q1)
SELECT
    return_flag,
    line_status,
    SUM(quantity) AS sum_qty,
    SUM(extended_price) AS sum_base_price,
    SUM(extended_price * (1 - discount)) AS sum_disc_price,
    SUM(extended_price * (1 - discount) * (1 + tax)) AS sum_charge,
    AVG(quantity) AS avg_qty,
    AVG(extended_price) AS avg_price,
    AVG(discount) AS avg_disc,
    COUNT(*) AS count_order
FROM
    {{ ref('stg_tpch__lineitem') }}
WHERE
    ship_date <= DATEADD(DAY, -90, DATE '1998-12-01')
GROUP BY
    return_flag,
    line_status
ORDER BY
    return_flag,
    line_status
