select distinct num as ConsecutiveNums
from
(select num,lead(num) over(order by id) as next,lag(num) over(order by id) prev
from logs) t1
where t1. num = t1.next and t1.num = t1.prev
