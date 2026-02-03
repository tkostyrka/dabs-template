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
	        {{ ref('stg_tpch__part') }}         AS p
INNER JOIN  {{ ref('stg_tpch__partsupp') }}      AS ps ON p.part_id = ps.part_id
INNER JOIN  {{ ref('stg_tpch__supplier') }}      AS s  ON ps.supplier_id = s.supplier_id
INNER JOIN  {{ ref('stg_tpch__nation') }}        AS n  ON s.nation_id = n.nation_id
INNER JOIN  {{ ref('stg_tpch__region') }}        AS r  ON n.region_id = r.region_id

where 1=1
and ps.supply_cost = (
    select
        min(ps.supply_cost)
    from
                {{ ref('stg_tpch__partsupp') }}      AS ps
    INNER JOIN  {{ ref('stg_tpch__supplier') }}      AS s  ON ps.supplier_id = s.supplier_id
    INNER JOIN  {{ ref('stg_tpch__nation') }}        AS n  ON s.nation_id = n.nation_id
    INNER JOIN  {{ ref('stg_tpch__region') }}        AS r  ON n.region_id = r.region_id
)
