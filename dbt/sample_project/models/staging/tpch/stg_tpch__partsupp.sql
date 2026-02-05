{{ config(
    materialized='view',
    enabled=true
) }}


WITH source AS (

    SELECT *
    FROM {{ source('tpch', 'partsupp') }}

),

renamed AS (

    SELECT
        ps_partkey AS part_id,
        ps_suppkey AS supplier_id,
        ps_availqty AS available_quantity,
        ps_supplycost AS supply_cost,
        ps_comment AS comment

    FROM source

)

SELECT * FROM renamed
