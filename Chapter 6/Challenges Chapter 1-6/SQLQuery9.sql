-- Update: Un tamam products ki price 10% barha dein jin ka stock 5 se kam hai.

UPDATE Products
SET 
	Price = Price + (Price * 0.10)
	WHERE Stock = 5

 