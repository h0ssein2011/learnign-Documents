{{
    config(
        materialized='table'
    )
}}
with customers as (
select  customer_id
        , customer_name
from {{ ref('int_js__customers') }}
)
, customer_orders as (
    select customer_id 
        , date(min(ordered_at)) as first_order_date
        , date(max(ordered_at)) as last_order_date
        , count(order_id) as number_of_orders
        , sum(order_total) as total_order
    from {{ ref('int_js__orders') }}
    group by 1
)
-- ranked customers by number_of_orders
, ranked_customer as (
    select * 
    , rank() over(order by number_of_orders  desc) as rank_customer
    from customer_orders 
)

select c.*
    , co.first_order_date
    , co.last_order_date
    , co.number_of_orders
    , co.rank_customer
from customers c 
join ranked_customer co on c.customer_id = co.customer_id
order by rank_customer