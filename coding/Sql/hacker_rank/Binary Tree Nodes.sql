-- https://www.hackerrank.com/challenges/binary-search-tree-1
*/
with root as
(select N
 from BST
where P IS NULL
), leaf as
(select N
 from BST
where N not in (select distinct P from BST where P is not NULL) and P IS NOT NULL )
select N,case when N in (select * from root) then  'Root'
              when N in (select * from leaf) then  'Leaf'
              else 'Inner' end as types
from BST
order by N