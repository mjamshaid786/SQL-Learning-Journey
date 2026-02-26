-- Har table mein kam se kam 5-5 records insert karein.

INSERT INTO Products (ProdID, Name, Category, Price, Stock, SupplierName)
	VALUES --(1, 'Mouse', 'Electronics', 500, 55, 'DigiTech'),
		   (2, 'Chair', 'Furniture', 2500, 15, 'BabuLohar'),
		   (3, 'Keyboard', 'Electronics', 1500, 25, 'DigiTech'),
		   (4, 'Table', 'Furniture', 5500, 5, 'BabuLohar'),
		   (5, 'USB', 'Electronics', 900, 45, 'DigiTech')

select * from Products