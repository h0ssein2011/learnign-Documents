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
--http:----www.postgresqltutorial.com--postgresql-window-function--


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


--case https://pgexercises.com/questions/joins/threejoin2.html
select mems.firstname || ' ' || mems.surname as member,
	facs.name as facility,
	case
		when mems.memid = 0 then
			bks.slots*facs.guestcost
		else
			bks.slots*facs.membercost
	end as cost
        from
                cd.members mems
                inner join cd.bookings bks
                        on mems.memid = bks.memid
                inner join cd.facilities facs
                        on bks.facid = facs.facid
        where
		bks.starttime >= '2012-09-14' and
		bks.starttime < '2012-09-15' and (
			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or
			(mems.memid != 0 and bks.slots*facs.membercost > 30)
		)
order by cost desc;


-- subquery
select concat(firstname,' ',surname) as member,
(
 select  concat(firstname,' ',surname) as recommender
  from cd.members recs
  where recs.memid=mems.recommendedby
  )

from cd.members mems
order by member

--month in postgresql
select facid,extract(month from starttime) as month ,sum(slots) as "Total Slots"

from cd.bookings
where
		starttime >= '2012-01-01'
		and starttime < '2013-01-01'
group by facid,month
order by facid,month

--case & aggregate
select fac.name,
sum( slots *
case
	when bks.memid=0 then fac.guestcost
	else fac.membercost

end ) revenue

from cd.facilities fac
inner join cd.bookings bks
on bks.facid = fac.facid

group by fac.name
order by revenue


-- select all rows counts
select (select count(*) from cd.members),firstname,surname

from cd.members
order by joindate

--row number in postgresql
select ROW_NUMBER() over() as row_number ,firstname,surname
from cd.members
order by joindate


--ntile
select name, case when class=1 then 'high'
		when class=2 then 'average'
		else 'low'
		end revenue
	from (
		select facs.name as name, ntile(3) over (order by sum(case
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) desc) as class
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as subq
order by class, name;


--limit agg fucntion
select name, revenue from (
	select facs.name, sum(case
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) as revenue
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as agg where revenue < 1000
order by revenue;
