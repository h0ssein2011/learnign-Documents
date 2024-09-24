-- CREATE TABLE events (
--     business_id INT,
--     event_type VARCHAR(20),
--     occurrences INT
-- );

-- INSERT INTO events (business_id, event_type, occurrences) VALUES
-- (1, 'reviews', 7),
-- (3, 'reviews', 3),
-- (1, 'ads', 11),
-- (2, 'ads', 7),
-- (3, 'ads', 6),
-- (1, 'page views', 3),
-- (2, 'page views', 12);

/* input : events table
conditions:
    - business with more than one active event
    - active event: occurance greater than average occurance event type

output:
- business ids which are active

*/
with grouped as 
(select * ,case when occurrences >= AVG(occurrences *1.0)  over (PARTITION by event_type) then 1 else 0 end as is_above_avg
from Events) , group_by as 
(select business_id ,sum(is_above_avg) as sums
from grouped
GROUP by business_id
)
select business_id 
from group_by
WHERE sums > 1
