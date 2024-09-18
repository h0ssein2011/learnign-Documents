with names as (
select name + "(" + left(occupation,1) + ")" as name
 from occupations
 order by name
 OFFSET 0 ROWS
), occs_group as
 (
 select occupation,count(*) as counts
 from occupations
 group by occupation
 order by count(*),occupation
 OFFSET 0 ROWS
 )
 select name from names
 union all
 select "There are a total of " + cast(counts as char(10)) + lower(occupation) + "s." as txt
 from occs_group