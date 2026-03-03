-- uSING DATEADD() FUNCTION...

SELECT 
	OrderDate,
	DATEADD(year, 2, OrderDate) AS [Incr. Year],
	DATEADD(month, -3, DATEADD(year, 2, OrderDate)) AS [Decr. month],
	DATEADD(day, 7, DATEADD(month, -3, DATEADD(year, 2, OrderDate))) AS [Incr. Day]
FROM Sales.Orders