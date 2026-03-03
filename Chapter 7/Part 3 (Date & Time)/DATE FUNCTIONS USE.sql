-- show all the orders that were placed in the month of february

SELECT
	OrderDate,
	MONTH(OrderDate) month,
	DATENAME(month, OrderDate) mName
FROM Sales.Orders
WHERE MONTH(OrderDate) = 2

