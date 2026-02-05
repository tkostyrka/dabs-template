-- TPC-H/TPC-R National Market Share Query (Q8)

select
    nation,
    order_year,
    sum(volume) as volume,
    sum(volume)
    / sum(sum(volume)) over (partition by order_year) as market_share

from
    (
        select
            n2.nation_name as nation,
            extract(year from o.order_date) as order_year,
            l.extended_price * (1 - l.discount) as volume
        from
            {{ ref('stg_tpch__part') }} as p
        inner join {{ ref('stg_tpch__lineitem') }} as l on p.part_id = l.part_id
        inner join
            {{ ref('stg_tpch__supplier') }} as s
            on l.supplier_id = s.supplier_id
        inner join {{ ref('stg_tpch__orders') }} as o on l.order_id = o.order_id
        inner join
            {{ ref('stg_tpch__customer') }} as c
            on o.customer_id = c.customer_id
        inner join
            {{ ref('stg_tpch__nation') }} as n1
            on c.nation_id = n1.nation_id
        inner join
            {{ ref('stg_tpch__nation') }} as n2
            on s.nation_id = n2.nation_id
        inner join
            {{ ref('stg_tpch__region') }} as r
            on n1.region_id = r.region_id
    ) as all_nations
group by
    order_year, nation
order by
    order_year, nation
