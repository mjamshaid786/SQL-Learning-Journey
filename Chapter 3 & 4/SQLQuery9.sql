-- change the score of customer 5

select * from customers
UPDATE customers
SET score = 450
WHERE id = 5