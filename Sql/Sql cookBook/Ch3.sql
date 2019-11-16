
select deptno from dept where deptno not in (select deptno from emp)

s