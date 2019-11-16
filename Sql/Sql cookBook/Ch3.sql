
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



