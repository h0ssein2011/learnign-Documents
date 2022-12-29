--   1- How many pizzas were ordered?
select count(distinct order_id  )
FROM pizza_runner.customer_orders



-- 2- How many unique customer orders were made?
select count(distinct customer_id) as uq_customers
FROM pizza_runner.customer_orders


-- 3How many successful orders were delivered by each runner?
with Clean_runner_orders_CTE as 
(select order_id,runner_id,pickup_time, 
  translate(distance,'km,null','') as distance,
  translate(duration,'minutes,mins,null','') as duration,
 case when cancellation in ('','null') then NULL else cancellation end as cancellation

FROM pizza_runner.runner_orders
 )
 
 select runner_id ,count(distinct order_id )
 from Clean_runner_orders_CTE
 where cancellation is NULL
 group by 1


-- 4How many of each type of pizza was delivered?
-- # order id 3 was contain two type of pizza so number of delivery is 2 times
select pn.pizza_name , count(distinct c.order_id )
FROM pizza_runner.customer_orders c
join pizza_runner.runner_orders r
ON r.order_id = c.order_id
join pizza_runner.pizza_names pn
ON c.pizza_id = pn.pizza_id
where r.pickup_time IS NOT NULL
group by 1

--5- How many Vegetarian and Meatlovers were ordered by each customer?
select c.customer_id ,pn.pizza_name , count(distinct c.order_id )
FROM pizza_runner.customer_orders c
join pizza_runner.pizza_names pn
ON c.pizza_id = pn.pizza_id
group by 1 ,2

--6-What was the maximum number of pizzas delivered in a single order?
select t.count_pizas from
(
select c.order_id , count(distinct c.pizza_id ) as count_pizas
FROM pizza_runner.customer_orders c
group by 1
order by 2 Desc
) t
limit 1

--7 For each customer, how many delivered pizzas had at least 1 change and how many had no changes?
WITH cleand_orders as 
(select * , 
case when  exclusions in ('null',NULL,'')  then NULL else exclusions end exclusions_cleaned,
case when  extras in ('null',NULL,'')  then NULL else extras end extras_cleaned

from pizza_runner.customer_orders)
select customer_id ,sum( case when (exclusions_cleaned is NULL) and (extras_cleaned is NULL)    
                   			then 0 else 1 end) as with_change,
                   sum( case when (exclusions_cleaned is NULL) and (extras_cleaned is NULL)    
                   			then 1 else 0 end) as with_out_change
                   
              
from cleand_orders
group by 1
order by 1
