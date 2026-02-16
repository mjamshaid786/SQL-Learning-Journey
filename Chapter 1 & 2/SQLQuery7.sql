/* Select all customers and sort the results
by country name and then by highest score first.*/

SELECT *
FROM customers
ORDER BY
	country ASC,
	score DESC