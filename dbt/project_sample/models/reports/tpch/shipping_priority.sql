-- TPC-H/TPC-R Shipping Priority Query (Q3)
select
    l.order_id,
    o.order_date,
    o.ship_priority,
    sum(l.extended_price * (1 - l.discount)) as revenue
from
    {{ ref('stg_tpch__customer') }} as c
inner join {{ ref('stg_tpch__orders') }} as o on c.customer_id = o.customer_id
inner join {{ ref('stg_tpch__lineitem') }} as l on o.order_id = l.order_id
where 1 = 1
group by
    l.order_id,
    o.order_date,
    o.ship_priority
