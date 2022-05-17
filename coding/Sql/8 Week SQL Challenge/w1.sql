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
sales_CTE as
(SELECT s.*, mn.product_name ,dense_rank() over( PARTITION by s.customer_id order by order_date ASC ) as ranks
FROM dannys_diner.sales s
 join dannys_diner.members m
 ON s.customer_id = m.customer_id
 join dannys_diner.menu mn
 ON mn.product_id = s.product_id
 where s.order_date > m.join_date
  )
  select customer_id ,product_name,order_date
  from sales_CTE
  where ranks =1

-- 7. Which item was purchased just before the customer became a member?
with
sales_CTE as
(SELECT s.*, mn.product_name ,dense_rank() over( PARTITION by s.customer_id order by order_date ASC ) as ranks
FROM dannys_diner.sales s
 join dannys_diner.members m
 ON s.customer_id = m.customer_id
 join dannys_diner.menu mn
 ON mn.product_id = s.product_id
 where s.order_date < m.join_date
  )
  select customer_id ,product_name,order_date
  from sales_CTE
  where ranks =1


-- 8. What is the total items and amount spent for each member before they became a member?
with
sales_CTE as
(SELECT s.*,mn.price
FROM dannys_diner.sales s
 join dannys_diner.members m
 ON s.customer_id = m.customer_id
 join dannys_diner.menu mn
 ON mn.product_id = s.product_id
 where s.order_date < m.join_date
  )
  select  customer_id,count(*) as total_items ,sum(price) as spent_amount 
  from sales_CTE s  
  group by 1

-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
with Sales_CTE as 
(SELECT s.*,mn.price ,
case when s.product_id=1 then mn.price * 10 * 2 else  mn.price * 10 end as points
FROM dannys_diner.sales s
 join dannys_diner.menu mn
 ON mn.product_id = s.product_id)
 
 select customer_id ,sum(points) as points
 from Sales_CTE
 group by 1
 order by 1

-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
with Sales_CTE as 
(SELECT s.*,mn.price ,
case when s.product_id=1 then mn.price * 10 * 2 
 when s.order_date >= m.join_date and  s.order_date < m.join_date + 7 
 							then mn.price * 10 * 2 else  mn.price * 10 end as points
FROM dannys_diner.sales s
 JOIN dannys_diner.members m
 ON m.customer_id = s.customer_id
 join dannys_diner.menu mn
 ON mn.product_id = s.product_id
where EXTRACT(MONTH FROM s.order_date::DATE) = 1
)
 
 select customer_id ,sum(points) as points
 from Sales_CTE
 
 group by 1
 order by 1
