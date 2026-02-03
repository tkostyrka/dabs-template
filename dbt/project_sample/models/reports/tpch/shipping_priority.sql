-- TPC-H/TPC-R Shipping Priority Query (Q3)
select
	l.order_id,
	sum(l.extended_price * (1 - l.discount)) as revenue,
	o.order_date,
	o.ship_priority
from
	        {{ ref('stg_tpch__customer') }} AS c
INNER JOIN  {{ ref('stg_tpch__orders') }} AS o ON c.customer_id = o.customer_id
INNER JOIN  {{ ref('stg_tpch__lineitem') }} AS l ON l.order_id = o.order_id
where 1=1
group by
	l.order_id,
	o.order_date,
	o.ship_priority
