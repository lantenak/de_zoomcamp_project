{{
    config
    (
        materialized='table',
        unique_key='primary_key',
        partition_by=
        {
            'field': 'status_dcd',
            'data_type': 'int64',
            'range':
            {
                'start': 1800,
                'end': 2020,
                'interval': 10
            }
        },
        cluster_by='desig_eng'
    )
}}

select
    {{ dbt_utils.generate_surrogate_key(['name', 'desig_eng', 'status_yr']) }} as primary_key,
    cast(NAME as string) as name,
    cast(DESIG_ENG as string) as desig_eng,
    cast(STATUS_YR as int) as status_yr,
    {{ get_status_year_decade('status_yr') }} as status_dcd

from {{ source('staging', 'protected_areas') }}

-- dbt build --select stg_protected_areas.sql --var 'is_test_run: false'
{% if var('is_test_run', default='true') %}

    limit 100

{% endif%}