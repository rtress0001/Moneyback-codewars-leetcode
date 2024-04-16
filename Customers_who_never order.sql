
select Customers.name as 'Customers'
from Customers
left join Orders on Orders.CustomerId = Customers.id
where Orders.id is NULL
