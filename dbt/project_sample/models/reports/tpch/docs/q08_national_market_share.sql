-- TPC-H/TPC-R National Market Share Query (Q8)

select
    nation,
	order_year,
	sum(volume) as volume,
    sum(volume) / sum(sum(volume)) over (partition by order_year) as market_share

from
	(
		select
			extract(year from o.order_date)       as order_year,
			l.extended_price * (1 - l.discount)   as volume,
			n2.nation_name                            as nation
		from
		                {{ ref('stg_tpch__part') }}       AS p
			INNER JOIN  {{ ref('stg_tpch__lineitem') }}   AS l      ON p.part_id = l.part_id
			INNER JOIN  {{ ref('stg_tpch__supplier') }}   AS s      ON l.supplier_id = s.supplier_id
			INNER JOIN  {{ ref('stg_tpch__orders') }}     AS o      ON l.order_id = o.order_id
			INNER JOIN  {{ ref('stg_tpch__customer') }}   AS c      ON o.customer_id = c.customer_id
			INNER JOIN  {{ ref('stg_tpch__nation') }}     AS n1     ON c.nation_id = n1.nation_id
			INNER JOIN  {{ ref('stg_tpch__nation') }}     AS n2     ON s.nation_id = n2.nation_id
			INNER JOIN  {{ ref('stg_tpch__region') }}     AS r      ON n1.region_id = r.region_id
	) as all_nations
group by
	order_year, nation
order by
	order_year, nation
