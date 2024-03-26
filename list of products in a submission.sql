# Write your MySQL query statement below
select 
    Products.product_name,
    sum(Orders.unit) as unit
from 
    Products
join 
    Orders on Products.product_id = Orders.product_id
where 
    Orders.order_date between '2020-02-01' AND '2020-02-29'
group by
    Products.product_name
Having
    sum(Orders.unit) >= 100