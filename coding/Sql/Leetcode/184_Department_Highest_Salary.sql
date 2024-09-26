/* Write your T-SQL query statement below */
select Department,Employee , Salary
from
(select e.name as Employee,d.name as Department ,e.Salary, dense_rank() over(partition by d.id order by e.salary Desc) as Salary_order_dep
 from Employee e
 join Department d on e.departmentId = d.id) t1
 where t1.Salary_order_dep = 1
