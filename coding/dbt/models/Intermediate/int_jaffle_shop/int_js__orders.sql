--stg_js__orders
{{
    config(
        materialized='table'
    )
}}

with orders as (
select order_id
    , customer_id
    , ordered_at 
    , store_id
    , subtotal
    , tax_paid 
    , order_total

from {{ ref('stg_js__orders') }}
)
select  *
from orders