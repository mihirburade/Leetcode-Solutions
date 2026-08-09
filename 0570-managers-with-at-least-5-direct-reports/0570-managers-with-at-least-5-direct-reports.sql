# Write your MySQL query statement below
select e2.name 
from Employee as e1
join Employee as e2
-- on e1.id = e2.managerId and e1.name = e2.name

on e1.managerId=e2.id
group by e2.id
having count(e2.id)>=5;

