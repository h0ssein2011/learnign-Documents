-- https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
with calc_scores as
(select h.hacker_id,h.name,s.challenge_id, max(s.score) as score
from Hackers h
join submissions s
on h.hacker_id = s.hacker_id
group by h.hacker_id,h.name,s.challenge_id
)
select hacker_id,name,sum(score) as score
from calc_scores
group by hacker_id,name
having sum(score) > 0
order by score desc ,hacker_id
;