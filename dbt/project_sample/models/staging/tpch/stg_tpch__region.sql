{{ config(
    materialized='view',
    enabled=true
) }}


WITH source AS (

    SELECT *
    FROM {{ source('tpch', 'region') }}

),

renamed AS (

    SELECT
        r_regionkey AS region_id,
        r_name AS region_name,
        r_comment AS comment

    FROM source

)

SELECT * FROM renamed
