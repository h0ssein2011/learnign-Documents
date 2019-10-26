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
