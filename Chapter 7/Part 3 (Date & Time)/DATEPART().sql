-- DATEPART()

SELECT 
	FirstName,
	Birthdate,
	DATEPART(day, BirthDate) day_dp
FROM Sales.Employees