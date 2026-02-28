-- TRANSFORM CUSTOMERS FIRST NAME TO LOWER CASE

SELECT 
	first_name,
LOWER(first_name) AS lower
FROM customers