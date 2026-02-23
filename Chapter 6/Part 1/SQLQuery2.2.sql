/*
get all customers along with their orders,
including orders without matching customers.
*/

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON o.customer_id = c.id  