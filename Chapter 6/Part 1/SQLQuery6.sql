/*
Get all orders without matching cutomers...
*/

SELECT * 
FROM customers AS c
RIGHT JOIN orders AS o
ON c.id = o.customer_id
WHERE c.id IS NULL