-- use master
-- CREATE TABLE [dbo].[DEPARTMENT](
-- 	[ID] [int] NOT NULL,
-- 	[NAME] [nvarchar](100) NULL,
-- PRIMARY KEY CLUSTERED 
-- (
-- 	[ID] ASC
-- )
-- ); 
-- CREATE TABLE [dbo].[EMPLOYEE](
-- 	[ID] [int] NOT NULL,
-- 	[DEPARTMENT_ID] [int] NULL,
-- 	[CHIEF_ID] [int] NULL,
-- 	[NAME] [nvarchar](100) NULL,
-- 	[SALARY] [money] NULL,
-- PRIMARY KEY CLUSTERED 
-- (
-- 	[ID] ASC
-- )
-- );
-- ALTER TABLE [dbo].[EMPLOYEE]  WITH CHECK ADD  CONSTRAINT [FK_EMPLOYEE_DEPARTMENT] FOREIGN KEY([DEPARTMENT_ID])
-- REFERENCES [dbo].[DEPARTMENT] ([ID]);
-- ALTER TABLE [dbo].[EMPLOYEE]  WITH CHECK ADD  CONSTRAINT [FK_EMPLOYEE_EMPLOYEE] FOREIGN KEY([CHIEF_ID])
-- REFERENCES [dbo].[EMPLOYEE] ([ID]);
-- ALTER TABLE [dbo].[EMPLOYEE] CHECK CONSTRAINT [FK_EMPLOYEE_DEPARTMENT]
-- ALTER TABLE [dbo].[EMPLOYEE] CHECK CONSTRAINT [FK_EMPLOYEE_EMPLOYEE];
-- INSERT [dbo].[DEPARTMENT] ([ID], [NAME]) VALUES (1, N'Department 1')
-- INSERT [dbo].[DEPARTMENT] ([ID], [NAME]) VALUES (2, N'Department 2')
-- INSERT [dbo].[DEPARTMENT] ([ID], [NAME]) VALUES (3, N'Department 3')
-- INSERT [dbo].[DEPARTMENT] ([ID], [NAME]) VALUES (4, N'Department 4')
-- INSERT [dbo].[DEPARTMENT] ([ID], [NAME]) VALUES (5, N'Department 5')
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (1, 1, NULL, N'Head of Department 1', 300000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (2, 5, NULL, N'Head of Department 5', 290000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (3, 2, NULL, N'Head of Department 2', 310000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (4, 4, NULL, N'Head of Department 4', 350000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (5, 1, 1, N'Employee 1 First Name', 100000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (6, 1, 1, N'Employee 2 First Name', 150000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (7, 1, 1, N'Employee 3 First Name', 310000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (8, 1, 1, N'Employee 4 First Name', 250000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (9, 2, 3, N'Employee 5 First Name', 250000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (10, 2, 3, N'Employee 6 First Name', 200000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (11, 5, 2, N'Employee 7 First Name', 150000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (12, 5, 2, N'Employee 8 First Name', 350000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (13, 4, 4, N'Employee 9 First Name', 100000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (14, 4, 4, N'Employee 10 First Name', 120000.0000)
-- INSERT [dbo].[EMPLOYEE] ([ID], [DEPARTMENT_ID], [CHIEF_ID], [NAME], [SALARY]) VALUES (15, 5, 4, N'Employee 11 First Name', 150000.0000)

/*
1-4 --> SUPerviser 
5--8> 1 
9--> 3 
10 --> 
*/

select * 
from employee

/* 
List employees who receive a salary higher than their immediate supervisor 
*/
SELECT e.ID, e.NAME, e.SALARY, s.NAME AS Supervisor_Name, s.SALARY AS Supervisor_Salary
FROM Employee e
Join Employee s  
on  e.CHIEF_ID = s.ID
 where e.SALARY > s.SALARY;

   
   
-- name of the person 
-- rank of salry for each dep


/*
List employees who receive the maximum 
salary in their department
*/
SELECT name,salary from 
(SELECT *,dense_rank() over(partition by DEPARTMENT_ID order by salary desc) as rn
   from employee 
  ) t 
  where t.rn = 1



/*
List the IDs of departments where the number 
of employees does not exceed 3 people
*/
SELECT DEPARTMENT_ID,count(NAME)
   from employee 
   group by DEPARTMENT_ID
   having count(NAME) <= 3



/*
List employees who do not have 
an assigned supervisor 
working in the same department
*/
SELECT e2.*,'--',e1.*
from employee e1 
join employee e2 on e1.CHIEF_ID = e2.id;


/*
Find the list of department IDs with the maximum 
total employee salary
*/
with sum_salary as 
(select  e.DEPARTMENT_ID ,sum(salary)  sum_salary
from employee e
GROUP by e.DEPARTMENT_ID)
,sorted_salary as 
(select * , DENSE_RANK() over(order by sum_salary desc) as rank
 from sum_salary)
 select * 
 from sorted_salary
 where rank = 1




/*
question : List the top two employees with the highest salary in each department

-- rank employees in each dep based salary 

*/
select * 
from 
( select * , DENSE_RANK() over(PARTITION by DEPARTMENT_ID order by salary desc) as rank
 from employee
 ) T 
 where T.rank <= 2


/*
Question:
List the departments that have less than three employees, and for each of those departments
, display the department name along with the average salary of its employees.

*/

SELECT DEPARTMENT_ID,avg(SALARY) as avg_salary
   from employee 
   group by DEPARTMENT_ID
   having count(NAME) >= 3;

/*
Question:
Given an Employee table with columns ID, NAME, SALARY, and MANAGER_ID 
(where MANAGER_ID refers to the ID of the employee’s manager), write a query to 
list each employee along with their manager’s name. 
Additionally, include only those employees whose salary is within 50 percent of their manager's salary.
*/

select e.NAME as employee_name ,s.NAME as boss_name,e.SALARY as employee_salary ,s.SALARY as boss_salary
from employee e 
join employee s 
on e.CHIEF_ID = s.ID 
where e.SALARY*1.0 <= s.SALARY * 0.1

/*
Write a query to find each department’s highest-paid employee, along with the 
name of the employee's manager. If the employee has no manager, display “No Manager” instead.
*/
select t.Name as emplyee_name , t.SALARY as employee_salary,
   case when s.NAME is null then 'No Manager' else s.NAME end  as boss_name    
from
(select e.* ,DENSE_RANK() over(partition by e.DEPARTMENT_ID order by e.Salary desc)  as rn
from employee e
) as t
left join employee s ON t.CHIEF_ID = s.ID 
WHERE t.rn=1


/*

Write a query to find the second-highest salary in each department. For each of these employees, display:

the DEPARTMENT_ID
the employee’s name and salary
their manager’s name and salary (or “No Manager” if they don’t have a manager).
If a department has fewer than two employees, it should not appear in the results.
*/



