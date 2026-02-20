/*Retrieve all ccustomers who are either
from the USA or have a score greater than 500.*/

SELECT * FROM Customers

SELECT * 
FROM Customers
WHERE country = 'USA' OR score > 500