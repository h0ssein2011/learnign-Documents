
select deptno from dept where deptno not in (select deptno from emp)
-- 
select d.* 
from dept d left join emp
on emp.deptno = d.deptno
where emp.deptno is Null

--My solution
select * from dept
where deptno not in (select distinct deptno from emp)


-- add table bounes
create table emp_bonus( EMPNO  integer,
			  RECEIVED date,
			  TYPE integer	)
			  
insert into emp_bonus(EMPNO,RECEIVED,TYPE)
values(7900 , '14-MAR-2005'  , 2),(7788 , '14-MAR-2005' ,3)

select * from emp_bonus
----Recipe 3.6. Adding Joins to a Query Without Interfering with Other Joins

select e.Ename ,d.LOC, b.RECEIVED 
from emp e left join dept d
on e.deptno=d.deptno 
left join emp_bonus b
on b.empno = e.empno

-- scalar query solution
select  e.Ename ,d.LOC,(select received from emp_bonus  b 
							 where e.empno = b.empno) as received
from emp e left join dept d
on e.deptno=d.deptno 


-- Recipe 3.7. Determining Whether Two Tables Have the Same Data

create view V 
as 
select * from emp where deptno !=10
union all
select * from emp where ename = 'WARD'

select * from V

(
select empno ,ename,job,mgr,hiredate,sal,comm,deptno ,count(*) from V
group by empno ,ename,job,mgr,hiredate,sal,comm,deptno 

except 

select empno ,ename,job,mgr,hiredate,sal,comm,deptno ,count(*) from emp
group by empno ,ename,job,mgr,hiredate,sal,comm,deptno )

union all
(
select empno ,ename,job,mgr,hiredate,sal,comm,deptno ,count(*) from emp
group by empno ,ename,job,mgr,hiredate,sal,comm,deptno 

except 

select empno ,ename,job,mgr,hiredate,sal,comm,deptno ,count(*) from V
group by empno ,ename,job,mgr,hiredate,sal,comm,deptno )


--Recipe 3.8. Identifying and Avoiding Cartesian Products
--You want to return the name of each employee in department 10 along with the location of the department.

select e.ename,d.LOC
from emp e inner join dept d
on e.deptno = d.deptno
where e.deptno=10



--Recipe 3.9. Performing Joins when Using Aggregates
--find the sum of the salaries for employees in department 10 along with the sum of their bonuses
select * from emp_bonus

create table emp_bonus( EMPNO  integer,
			  RECEIVED date,
			  TYPE integer	)
			  
insert into emp_bonus(EMPNO,RECEIVED,TYPE)
values (7934, '17-MAR-2005'  ,      1),
	 (7934 ,'15-FEB-2005 ' ,        2),
	 (7839 ,'15-FEB-2005 '  ,       3),
	( 7782 , '15-FEB-2005 '  ,       1)

select * from emp_bonus

select deptno ,sum(distinct sal) ,sum(bonus)
from (
select e.empno,e.ename,e.deptno ,e.sal,e.sal * case when eb.Type = 1 then .1
													when eb.Type = 2 then .2
											 		else .3 end as bonus 
	from emp e , emp_bonus eb
	where  e.empno = eb.empno
	and deptno =10
) x
group by deptno

 
--Recipe 3.12. Using NULLs in Operations and Comparisons
--you want to find all employees in EMP whose commission (COMM) is less than the commission of employee "WARD". 
select ename, comm ,coalesce(comm,0)
from emp
where  COALESCE(comm ,0)  < (select comm from emp where ename='WARD')
	
