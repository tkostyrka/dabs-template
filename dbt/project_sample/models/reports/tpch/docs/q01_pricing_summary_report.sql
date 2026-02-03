-- TPC-H/TPC-R Pricing Summary Report Query (Q1)
select
    return_flag,
    line_status,
    sum(quantity) as sum_qty,
    sum(extended_price) as sum_base_price,
    sum(extended_price * (1 - discount)) as sum_disc_price,
    sum(extended_price * (1 - discount) * (1 + tax)) as sum_charge,
    avg(quantity) as avg_qty,
    avg(extended_price) as avg_price,
    avg(discount) as avg_disc,
    count(*) as count_order
from
    {{ ref('stg_tpch__lineitem') }}
where
    ship_date <= dateadd(day, -90, date '1998-12-01')
group by
    return_flag,
    line_status
order by
    return_flag,
    line_status
