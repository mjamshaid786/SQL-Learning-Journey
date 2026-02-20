-- Retrieve customers either from USA or Germany


select * from customers

select *
from customers
where country IN ('Germany', 'USA')