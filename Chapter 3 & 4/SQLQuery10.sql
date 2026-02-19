-- update score of customer 6 and update country to UK

select * from customers
UPDATE customers
	SET score = 970,
		country = 'UK'
	WHERE id = 6