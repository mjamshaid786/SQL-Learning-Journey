-- get the first 2 character of each name from first_name's of customers

SELECT
	first_name,
	LEFT(TRIM(first_name), 2) AS TrimName
	
	
FROM customers