-- GET THE NAMES OF CUSTOMERS AFTER REMOVING FIRST CHARACTER..

SELECT 
	first_name,
	SUBSTRING(TRIM(first_name), 2, LEN(first_name)) AS sub_name
FROM customers