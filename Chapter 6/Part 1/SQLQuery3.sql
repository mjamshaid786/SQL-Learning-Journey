/*
Get all customers along with their orders,
including orders without matching customers.
*/

SELECT *
FROM orders AS o
LEFT JOIN customers AS c
ON o.customer_id = c.id