-- GET THE LAST 2 LETTERS FORM FIRST_NAME...

SELECT
	first_name,
	RIGHT(first_name, 2) AS Last2Char
FROM customers