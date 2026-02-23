/*
Get all customers and all orders,
even if there's no match
*/

SELECT 
	c.id,
	c.first_name,
	c.country,
	o.order_id,
	o.sales
FROM customers as c
FULL JOIN orders AS o
ON c.id = o.customer_id