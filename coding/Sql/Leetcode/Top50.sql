/*markdown
### [1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/)
**Difficulty:** Medium  
**Topic:** Left Join / Aggregate Functions
*/

# Write your MySQL query statement below
-- cr : confirmed / requests
-- round 2 decimals
with tbl as (
select s.user_id
    , coalesce(count(c.user_id),0) as total_request
    , coalesce(count(case when action = "confirmed" then c.user_id end),0) as confirmed_msg
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by 1
)
select user_id, case when total_request = 0 then 0
                else round(confirmed_msg / total_request,2) end
                    as confirmation_rate
from tbl