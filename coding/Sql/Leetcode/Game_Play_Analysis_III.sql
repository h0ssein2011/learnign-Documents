select player_id , event_date, sum() over(partition by player_id order by event_date)
from activity