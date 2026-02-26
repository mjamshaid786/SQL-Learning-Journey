-- Online_Sales: SaleID (PK), ProdID (FK), Customer, SaleDate, Qty.

CREATE TABLE Online_Sales (
	SalesID INT NOT NULL,
	ProdID INT NOT NULL,
	Customer VARCHAR (20),
	SaleDate DATE,
	Qty INT,

	CONSTRAINT pk_SalesID PRIMARY KEY (SalesID),
	CONSTRAINT fk_ProdID FOREIGN KEY (ProdID)
	REFERENCES Products (ProdID)
)

