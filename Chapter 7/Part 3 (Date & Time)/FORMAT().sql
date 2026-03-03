--Learning FORMAT() Function...

SELECT
	OrderDate,
	FORMAT(OrderDate, 'dd/MM/yy') f_Date
FROM Sales.Orders