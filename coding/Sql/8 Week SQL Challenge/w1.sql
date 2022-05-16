/* --------------------
   Case Study Questions
   --------------------*/


-- 1. What is the total amount each customer spent at the restaurant?
SELECT
 customer_id ,count(product_id) as 	total_amount
FROM dannys_diner.sales
group by 1

-- 2. How many days has each customer visited the restaurant?
select 
   customer_id,
   count(distinct order_date) as days_visited
from dannys_diner.sales
group by 1

-- 3. What was the first item from the menu purchased by each customer?
select 
   customer_id,min(order_date) as first_purchase_date
from dannys_diner.sales
group by 1

-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
with purchase_times as 
(
select product_id ,count(*) 
 from dannys_diner.sales
  group by 1
 order by 2 Desc
)
select * from purchase_times
limit 1

-- 5. Which item was the most popular for each customer?
with purchase_time as (
select customer_id ,product_id ,count(*) as pt
  from dannys_diner.sales
  group by 1 ,2
  order by 1,3 Desc
)
, rankings as 
(select 
    * ,rank() over(PARTITION BY customer_id order by pt Desc ) as ranks
 from purchase_time)
 select * from rankings
 where ranks =1





-- 6. Which item was purchased first by the customer after they became a member?
with
tr_status as
(SELECT s.*, 
  case when s.order_date > m.join_date or m.join_date is null  then 'after_join' else 'before_join' end as transactions 
 -- ,case when m.join_date is null then s.order_date else m.join_date end as join_date
FROM dannys_diner.sales s
 left join dannys_diner.members m
 ON s.customer_id = m.customer_id
  )
 , Min_Purchase as 
  (select customer_id ,product_id , min(order_date)
  from tr_status
  where transactions = 'after_join'
  group by 1,2)
  
  select distinct customer_id ,mn.product_name
  from Min_Purchase mp
  join dannys_diner.menu mn
  ON mn.product_id = mp.product_id
  order by 1

-- 7. Which item was purchased just before the customer became a member?
with
tr_status as
(SELECT s.*, 
  case when s.order_date > m.join_date or m.join_date is null  then 'after_join' else 'before_join' end as transactions 
 -- ,case when m.join_date is null then s.order_date else m.join_date end as join_date
FROM dannys_diner.sales s
 left join dannys_diner.members m
 ON s.customer_id = m.customer_id
  )
 , Min_Purchase as 
  (select customer_id ,product_id , min(order_date)
  from tr_status
  where transactions = 'before_join'
  group by 1,2)
  
  select distinct customer_id ,mn.product_name
  from Min_Purchase mp
  join dannys_diner.menu mn
  ON mn.product_id = mp.product_id
  order by 1


-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
