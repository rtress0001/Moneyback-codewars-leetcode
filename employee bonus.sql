select employee_id,
    CASE
        when employee_id % 2 = 1 and left(name,1) != 'M' Then Salary
        Else 0
    end as bonus
from Employees
order by employee_id

