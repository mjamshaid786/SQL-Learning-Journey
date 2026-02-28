-- TRANSFORM CUSTOMERS FIRST NAME TO UPPER

SELECT 
	first_name,
	UPPER(first_name) AS Upper
FROM customers