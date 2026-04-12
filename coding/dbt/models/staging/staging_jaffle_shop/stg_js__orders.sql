--stg_js__orders
{{
    config(
        materialized='table'
    )
}}

with orders as (
select id as order_id
    , customer as customer_id
    , ordered_at 
    , store_id
    , subtotal
    , tax_paid 
    , order_total

from {{ source('dbt_tutorial', 'orders') }}
)
select  *
from orders