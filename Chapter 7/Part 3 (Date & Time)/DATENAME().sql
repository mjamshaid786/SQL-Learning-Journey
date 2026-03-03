--DATENAME()

SELECT 
	BirthDate,
	DATENAME(month, BirthDate) month,
	DATENAME(weekday, BirthDate) day
	
FROM Sales.Employees