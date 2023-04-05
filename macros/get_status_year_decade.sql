{#
    This macro returns the decade of status year
#}

{% macro get_status_year_decade(status_yr) %}

    (cast(concat(substring({{ status_yr }}, 1, 3), '0') as int))

{% endmacro %}