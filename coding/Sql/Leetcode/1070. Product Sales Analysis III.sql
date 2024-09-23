/* Write your T-SQL query statement below
input :
sales / product table
output:
    product_id, year,quantity, price for the first year
*/
with sorted as
(select p.product_id , s.year,s.quantity,s.price , dense_rank() over(partition by p.product_id
             order by s.year asc) as rn
from Sales s
join Product p on s.product_id = p.product_id)
select product_id , year as first_year,quantity,price
from sorted
where rn = 1


