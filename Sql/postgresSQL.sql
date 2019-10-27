select name,
CASE
    when monthlymaintenance >100 then 'expensive'
    else 'cheap'
END as  cost


from cd.facilities


/combine two columns from differnt

select surname
  from cd.members
UNION
  select name
  from
  cd.facilities

/subquery
  select firstname, surname, joindate
  	from cd.members
  	where joindate =
  		(select max(joindate)


/case sensetive search
select * from cd.facilities
where name ILIKE 'tennis%'

select memid, telephone from cd.members where telephone ~ '[()]';


/REPLACE characters
select memid, translate(telephone, '-() ', '') as telephone
    from cd.members
    order by memid;


/join
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
