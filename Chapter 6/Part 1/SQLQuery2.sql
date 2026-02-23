--select the only customers who has placed orders
SELECT * FROM customers;
SELECT * FROM orders;

SELECT 
	c.id,
	c.first_name,
	c.country,
	o.order_id,
	o.sales
FROM customers AS c
INNER JOIN orders AS o
ON id = customer_id