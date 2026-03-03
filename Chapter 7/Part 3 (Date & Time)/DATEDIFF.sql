--CALCULATE THE AGE OF EMPLOYEES...

SELECT 
	BirthDate,
	DATEDIFF(year, BirthDate, GETDATE()) AS age
FROM Sales.Employees