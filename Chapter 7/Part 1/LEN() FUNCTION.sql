--Calculate the length of customer's first names..

SELECT 
	first_name,
	LEN(first_name) AS LenOfNames
FROM customers