-- Test to check if a column is greater than zero
-- This test will fail if any row in the column is less than or equal to zero
{% test greater_than_zero(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} <= 0
{% endtest %}
