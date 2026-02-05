-- TPC-H/TPC-R Minimum Cost Supplier Query (Q2)
select
    s.account_balance,
    s.supplier_name,
    n.nation_name,
    p.part_id,
    p.manufacturer,
    s.address,
    s.phone_number,
    s.comment
from
    {{ ref('stg_tpch__part') }} as p
inner join {{ ref('stg_tpch__partsupp') }} as ps on p.part_id = ps.part_id
inner join
    {{ ref('stg_tpch__supplier') }} as s
    on ps.supplier_id = s.supplier_id
inner join {{ ref('stg_tpch__nation') }} as n on s.nation_id = n.nation_id
inner join {{ ref('stg_tpch__region') }} as r on n.region_id = r.region_id

where
    1 = 1
    and ps.supply_cost = (
        select min(ps.supply_cost)
        from
            {{ ref('stg_tpch__partsupp') }} as ps
        inner join
            {{ ref('stg_tpch__supplier') }} as s
            on ps.supplier_id = s.supplier_id
        inner join
            {{ ref('stg_tpch__nation') }} as n
            on s.nation_id = n.nation_id
        inner join
            {{ ref('stg_tpch__region') }} as r
            on n.region_id = r.region_id
    )
