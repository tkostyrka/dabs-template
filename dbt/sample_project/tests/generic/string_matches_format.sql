-- This test checks if the values in a specified column of a model match a given regex pattern.
-- It will fail if any row in the column does not match the regex pattern.
{% test string_matches_format(model, column_name, regex_pattern) %}
    SELECT *
    FROM {{ model }}
    WHERE NOT {{ column_name }} RLIKE '{{ regex_pattern }}'
{% endtest %}
