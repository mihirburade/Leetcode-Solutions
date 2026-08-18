# Write your MySQL query statement below
select P.product_id, round(ifNull(sum(P.price*U.units)/sum(U.units),0),2) as average_price
from Prices as P
left join UnitsSold as U
on P.product_id = U.product_id
and P.start_date<=U.purchase_date and P.end_date>=U.purchase_date
group by P.product_id;
