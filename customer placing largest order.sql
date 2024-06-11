# Write your MySQL query statement below
select customer_number
from Orders
Group by customer_number
Order by Count(order_number) DESC
Limit 1;