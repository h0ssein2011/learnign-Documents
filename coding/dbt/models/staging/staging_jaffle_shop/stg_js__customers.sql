--stg_js__customers
{{
    config(
        materialized='view'
    )
}}

with customers as (
    select id,
    name 
    from {{ source('dbt_tutorial', 'customers') }}
)
select *
from customers