-- TPC-H/TPC-R National Market Share Query (Q8)

SELECT
    nation,
    order_year,
    SUM(volume) AS volume,
    SUM(volume)
    / SUM(SUM(volume)) OVER (PARTITION BY order_year) AS market_share

FROM
    (
        SELECT
            n2.nation_name AS nation,
            EXTRACT(YEAR FROM o.order_date) AS order_year,
            l.extended_price * (1 - l.discount) AS volume
        FROM
            {{ ref('stg_tpch__part') }} AS p
        INNER JOIN {{ ref('stg_tpch__lineitem') }} AS l ON p.part_id = l.part_id
        INNER JOIN
            {{ ref('stg_tpch__supplier') }} AS s
            ON l.supplier_id = s.supplier_id
        INNER JOIN {{ ref('stg_tpch__orders') }} AS o ON l.order_id = o.order_id
        INNER JOIN
            {{ ref('stg_tpch__customer') }} AS c
            ON o.customer_id = c.customer_id
        INNER JOIN
            {{ ref('stg_tpch__nation') }} AS n1
            ON c.nation_id = n1.nation_id
        INNER JOIN
            {{ ref('stg_tpch__nation') }} AS n2
            ON s.nation_id = n2.nation_id
        INNER JOIN
            {{ ref('stg_tpch__region') }} AS r
            ON n1.region_id = r.region_id
    ) AS all_nations
GROUP BY
    order_year, nation
ORDER BY
    order_year, nation
