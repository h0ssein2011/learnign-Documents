-- with CTE
with sorted as
(select p.project_id,p.employee_id,dense_rank() over(partition by p.project_id order by e.experience_years desc) as rank
from project p
join employee e on e.employee_id = p.employee_id)
select project_id,employee_id
from sorted
where rank = 1

-- with Subquery

select project_id,employee_id
from (select p.project_id,p.employee_id,dense_rank() over(partition by p.project_id order by e.experience_years desc) as rank
from project p
join employee e on e.employee_id = p.employee_id) tbl1
where rank = 1
