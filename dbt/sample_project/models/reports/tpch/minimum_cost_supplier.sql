-- TPC-H/TPC-R Minimum Cost Supplier Query (Q2)
SELECT
    s.account_balance,
    s.supplier_name,
    n.nation_name,
    p.part_id,
    p.manufacturer,
    s.address,
    s.phone_number,
    s.comment
FROM
    {{ ref('stg_tpch__part') }} AS p
INNER JOIN {{ ref('stg_tpch__partsupp') }} AS ps ON p.part_id = ps.part_id
INNER JOIN
    {{ ref('stg_tpch__supplier') }} AS s
    ON ps.supplier_id = s.supplier_id
INNER JOIN {{ ref('stg_tpch__nation') }} AS n ON s.nation_id = n.nation_id
INNER JOIN {{ ref('stg_tpch__region') }} AS r ON n.region_id = r.region_id

WHERE
    1 = 1
    AND ps.supply_cost = (
        SELECT MIN(psi.supply_cost)
        FROM
            {{ ref('stg_tpch__partsupp') }} AS psi
        INNER JOIN
            {{ ref('stg_tpch__supplier') }} AS si
            ON psi.supplier_id = si.supplier_id
        INNER JOIN
            {{ ref('stg_tpch__nation') }} AS ni
            ON si.nation_id = ni.nation_id
        INNER JOIN
            {{ ref('stg_tpch__region') }} AS ri
            ON ni.region_id = ri.region_id
    )
