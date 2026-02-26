-- Store_Sales: SaleID (PK), ProdID (FK), Customer, SaleDate, Qty.

CREATE TABLE Store_Sales (
	SaleID INT NOT NULL,
	ProdID INT NOT NULL,
	Customer VARCHAR NOT NULL,
	SaleDate DATE,
	Qty INT,
	CONSTRAINT pk_SaleID PRIMARY KEY (SaleID),
	CONSTRAINT fk2_ProdID FOREIGN KEY (ProdID)
	REFERENCES Products (ProdID)
)