{{
    config(
        materialized='table'
    )
}}

with customers as (
select *
from {{ ref('int_js__customers') }}
)
,
orders as (
    select *
    from {{ ref('int_js__orders') }}
)

select o.order_id
    , c.customer_name 
    , o.ordered_at
    , o.store_id
    , o.subtotal
    , o.tax_paid
    , o.order_total
from orders o 
join customers c on o.customer_id = c.customer_id