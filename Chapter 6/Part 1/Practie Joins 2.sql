/*
Using SalesDB, Retrieve a list of all orders, along with the related
cusomer, product, and emplyee details. For each order, display:
Order ID, Customer's name, Product name, Sales, Price, Sales person's name.
*/

SELECT 
	o.OrderID,
	o.Sales,
	c.FirstName AS CustomerFirstName,
	c.LastName AS CustomerLastName,
	p.Product,
	p.Price,
	e.FirstName AS SalesPersonFName,
	e.LastName AS SalesPersonLName
FROM Sales.Orders AS o
LEFT JOIN Sales.Customers AS c
ON o.CustomerID = c.CustomerID
LEFT JOIN Sales.Products AS p
ON o.ProductID = p.ProductID
LEFT JOIN Sales.Employees AS e
ON o.SalesPersonID = e.EmployeeID