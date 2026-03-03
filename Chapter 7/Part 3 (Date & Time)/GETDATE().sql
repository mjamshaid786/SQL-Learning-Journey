-- learning DAY(), MONTH(), YEAR() FUNCTIONS

SELECT  
EmployeeID,
FirstName,
BirthDate,
DAY(BirthDate) Day,
MONTH(BirthDate) Month,
YEAR(BirthDate) Year
FROM Sales.Employees