select name,
CASE
    when monthlymaintenance >100 then 'expensive'
    else 'cheap'
END as  cost


from cd.facilities


--combine two columns from differnt

select surname
  from cd.members
UNION
  select name
  from
  cd.facilities

--subquery
  select firstname, surname, joindate
  	from cd.members
  	where joindate =
  		(select max(joindate)


--case sensetive search
select * from cd.facilities
where name ILIKE 'tennis%'

select memid, telephone from cd.members where telephone ~ '[()]';


--REPLACE characters
select memid, translate(telephone, '-() ', '') as telephone
    from cd.members
    order by memid;


--join
select mem.memid,mem.surname,mem.telephone,bking.slots

from cd.members mem

left join

cd.bookings bking

ON mem.memid=bking.memid
where bking.slots=4


# return first 5 rows
select * from
cd.members
order by joindate DESC
fetch first
5 rows only


--add extra columns
select surname ,firstname,max(joindate) over (partition by recommendedby)

from
cd.members
order by joindate DESC


----rank function
select surname ,firstname,rank() over (PARTITION BY recommendedby order by joindate)

from
cd.members

----lag and lead columns data
select name,round(monthlymaintenance--1000) as mcost,lag(facid)  over(partition by name)

from
cd.facilities

----window fucntions in postgresql
----http:----www.postgresqltutorial.com--postgresql-window-function--


--join
select a.starttime
from cd.bookings a
inner join cd.members b
on
a.memid = b.memid
where
b.surname='Farrell' and b.firstname='David'


select bk.starttime as start ,fc.name as name
from cd.bookings bk
  inner join
  cd.facilities fc
          on
          bk.facid=fc.facid
where
	  fc.facid in (0,1) and
	  bk.starttime >= '2012-09-21'  and
	  bk.starttime < '2012-09-22'
order by bk.starttime

----left join
SELECT mems.firstname as memfname,mems.surname as memsname,
recs.firstname as recfname,recs.surname as recsname
from cd.members mems
left outer join cd.members recs
on mems.recommendedby=recs.memid

order by memsname,memfname

--OrderDetailsjoin 3 table
select distinct mems.firstname || ' '|| mems.surname as member,fac.name as facility
from cd.members mems
inner join
cd.bookings bks
		on mems.memid = bks.memid
inner join
cd.facilities fac
		on bks.facid=fac.facid
where fac.facid in (0,1)
order by member
