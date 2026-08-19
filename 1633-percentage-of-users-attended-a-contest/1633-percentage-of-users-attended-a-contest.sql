# Write your MySQL query statement below
select R.contest_id , round(count(R.user_id)*100/ (select count(*) from Users),2) as percentage
from Users as U
right join Register as R
on U.user_id = R.user_id
group by R.contest_id
order by percentage DESC,R.contest_id;