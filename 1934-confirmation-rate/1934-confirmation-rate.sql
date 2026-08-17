select S.user_id,round(ifnull(avg(action='confirmed'),0),2) as confirmation_rate
from Signups as S
left join Confirmations as C
on S.user_id = C.user_id
group by S.user_id;