-- CHECK THE SPACES IN CUSTOMER'S FIRSTNAME COLUMN

SELECT 
	first_name
FROM customers

WHERE first_name != TRIM(first_name)