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
  replace(cancellation,'null','') as cancellation1
 ,cancellation

FROM pizza_runner.runner_orders
 )
 
 select * from Clean_runner_orders_CTE
