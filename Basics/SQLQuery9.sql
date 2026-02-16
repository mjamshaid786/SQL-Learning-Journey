-- Find total score and total no. of customers for each country

SELECT
	country,
	SUM(score) AS total_score,
	COUNT(id) AS total_customers
FROM customers
GROUP BY country
HAVING SUM(score) > 800