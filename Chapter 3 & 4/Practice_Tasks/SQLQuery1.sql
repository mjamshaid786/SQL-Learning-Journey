-- (TASK-1)

CREATE TABLE Products (
	ProductID INT NOT NULL,
	ProductName VARCHAR(50) NULL,
	Category VARCHAR,
	Price DECIMAL NOT NULL,
	StockQuanity INT
	CONSTRAINT pk_Products PRIMARY KEY (ProductID)

)