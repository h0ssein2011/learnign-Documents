-- ch6
--Recipe 6.1. Walking a String
--You want to traverse a string to return each character as a row, but SQL lacks a loop operation. For example, you want to display the ENAME "KING" from table EMP as four rows, where each row contains just characters from "KING".
select substr(ename,iter.pos,1) as C
from (select ename from emp where ename='KING')  e ,
		(select id as pos from t10) iter
		where iter.pos <= length(e.ename)
		
select e.ename ,t.pos as b from	
(select ename from emp) e ,
(select id as pos from t10 )t



select substr(ename,iter.pos) as C,substr(ename,length(ename)- iter.pos+1 )
from (select ename from emp where ename='KING')  e ,
		(select id as pos from t10) iter
		where iter.pos <= length(e.ename)
		
select '''' as quote from t1

--Recipe 6.3. Counting the Occurrences of a Character in a String

select (length('10,CLARK,MANAGER') - length(replace('10,CLARK,MANAGER','R',''))) / length(',')

--Recipe 6.4. Removing Unwanted Characters from a String
--You want to remove specific characters from your data. Consider this result set:

select ename, replace(translate(ename,'AEIOU','aaaaa'),'a','') as striped1,
				sal,
				replace(cast(sal as char(4)),'0','') as striped2
from emp

select translate(cast(4353344 as char),'44','22')
select cast(4353344 as char(5)) 
select rpad('z',20,'z')


create table Data (
ename char,
sal integer
)

insert into Data (ename,sal)
values (SMITH,800),(ALLEN,1600),(WARD,1250),(JONES,2975),(MARTIN,1250),(BLAKE,2850),(CLARK,2450),(SCOTT,3000),(KING,5000),(TURNER,1500),(ADAMS,1100),(JAMES,950),(FORD,3000),(MILLER,1300)

--Recipe 6.5. Separating Numeric and Character Data
--You have (unfortunately) stored numeric data along with character data together in one column. You want to separate the character data from the numeric data. Consider the following result set:

create table Data1 (
ename char(10))
insert into Data1 (ename)
values ('SMITH800'),('ALLEN1600'),('WARD1250'),('JONES2975'),('MARTIN1250'),('BLAKE2850'),('CLARK2450'),('SCOTT3000'),('KING5000'),('TURNER1500'),('ADAMS1100'),('JAMES950'),('FORD3000'),('MILLER1300')

select ename ,length(ename) from data1

--solution

create View data2 (DATA) as 
select ename || sal
from emp

select * from data2

--my approach to copy the data 
select replace( translate(data,'0123456789','0000000000'),'0','') as ename ,
cast(replace(translate(lower(data),'abcdefghijklmnopqrstuvwxyz',rpad('z',26,'z')),'z','') as integer) as sal
 from data2 


select replace(
	
 translate(data1,'0123456789','0000000000'),'0','') as ename,
	 
	 cast(
	         replace(
	       translate(lower(data1),
	                 'abcdefghijklmnopqrstuvwxyz',
	                 rpad('z',26,'z')),'z','') as integer) as sal
	    from (
	  select ename||sal as data1
	   from emp
	        ) x


--Recipe 6.6. Determining Whether a String Is Alphanumeric
--You want to return rows from a table only when a column of interest contains no characters other than numbers and letters
 

create view V as
	select ename as data
	  from emp
	 where deptno=10
	 union all
	select ename||', $'|| cast(sal as char(4)) ||'.00' as data
	  from emp
	 where deptno=20
	 union all
	select ename|| cast(deptno as char(4)) as data
	  from emp
	 where deptno=30
	 
select * from v

 select data
	   from V
	  where translate(lower(data),
	                  '0123456789abcdefghijklmnopqrstuvwxyz',
	                  rpad('a',36,'a')) = rpad('a',length(data),'a')

select rpad('a',36,'a')

select data , translate(lower(data),'0123456789abcdefghijklmnopqrstuvwxyz',rpad('a',36,'a'))  translated,
			 rpad('a',length(data),'a')   fixed
from v

	select data, translate(lower(data),
	                  '0123456789abcdefghijklmnopqrstuvwxyz',
	                   rpad('a',36,'a'))
	  from V


--Recipe 6.7. Extracting Initials from a Name
--You want convert a full name into initials. Consider the following name: 	 Stewie Griffin


select replace(replace(translate(replace('Stewie Griffin','.',''),'bcdefghijklmnopqrstuvwxyz',rpad('#',26,'#')),'#',''),' ','.') || '.'
 from t1
 select replace(
	        replace(
	        translate(replace('Stewie Griffin', '.', ''),
	                  'abcdefghijklmnopqrstuvwxyz',
	                  rpad('#',26,'#') ), '#','' ),' ','.' ) ||'.'
	   from t1


create Table data3 (ename text)

insert into data3 (ename)
values ('ALLEN'),('TURNER'),('MILLER'),('JONES'),('JAMES'),('MARTIN'),('BLAKE'),('ADAMS'),('KING'),('WARD'),('FORD'),('CLARK'),('SMITH'),('SCOTT')

--Recipe 6.8. Ordering by Parts of a String
--You want to order your result set based on a substring. Consider the following records:

select * from data3

select ename from emp 
order by substr(ename,length(ename)-1,2)

--Recipe 6.9. Ordering by a Number in a String
--You want order your result set based on a number within a string. Consider the following view:

create view V as 
select  e.ename ||' '||
	        cast(e.empno as char(4))||' '||
	        d.dname as data
	  from emp e, dept d
	 where e.deptno=d.deptno
--my approach	
select data 
from v 	 
order by (select replace(
	translate(lower(data),'abcdefghijklmnopqrstuvwxyz','#'),'#','')) 

-- book approach
select data from V
order by
cast(
replace(
translate(data,
replace(
translate(data,'0123456789','##########'), '#',''),rpad('#',20,'#')),'#','') as integer)





--Recipe 6.11. Converting Delimited Data into a Multi-Valued IN-List

	   select ename,sal,deptno
	     from emp
	    where empno in (
	   select cast(empno as integer) as empno
	     from (
	   select split_part(list.vals,',',iter.pos) as empno
	     from (select id as pos from t10) iter,
	          (select ','||'7654,7698,7782,7788'||',' as vals
	             from t1) list
	   where iter.pos <=
	         length(list.vals)-length(replace(list.vals,',',''))
	         ) z
	   where length(empno) > 0
	         ) x




