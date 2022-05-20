--   1- How many pizzas were ordered?
select count(distinct order_id  )
FROM pizza_runner.customer_orders



-- 2- How many unique customer orders were made?
select count(distinct customer_id) as uq_customers
FROM pizza_runner.customer_orders


-- How many successful orders were delivered by each runner?
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


-- How many of each type of pizza was delivered?
-- # order id 3 was contain two type of pizza so number of delivery is 2 times
select pn.pizza_name , count(distinct c.order_id )
FROM pizza_runner.customer_orders c
join pizza_runner.runner_orders r
ON r.order_id = c.order_id
join pizza_runner.pizza_names pn
ON c.pizza_id = pn.pizza_id
where r.pickup_time IS NOT NULL
group by 1