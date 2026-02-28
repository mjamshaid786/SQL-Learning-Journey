-- Combine firstname and country from customers table in single column
--select * from customers
SELECT 
	first_name,
	country,
CONCAT (first_name, ' ', country) AS Name_Country
FROM customers