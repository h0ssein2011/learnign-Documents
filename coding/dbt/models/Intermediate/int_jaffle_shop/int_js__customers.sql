--int_js__customers
{{
    config(
        materialized='view'
    )
}}

with customers as (
    select id as customer_id,
    name as customer_name
    from {{ ref('stg_js__customers') }}
), aggregated_orders as (
    select customer_id
    , date(min(ordered_at))  as first_order_at
    , date(max(ordered_at) ) as last_order_at
    from {{ ref('stg_js__orders') }}
    group by 1
)
, final as (
select c.*
    ,o.first_order_at 
    ,o.last_order_at 
    , case when date_diff(current_date() , o.last_order_at  , Day) > 90 then 1 else 0 end as is_churn
from customers c 
left join  aggregated_orders o on o.customer_id = c.customer_id 

)
select * 
from final 