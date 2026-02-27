/* 1. Online_Sales aur Store_Sales ka sara data aik jagah jama karein 
(duplicates ke sath), taaki total revenue ka pata chal sake*/

/* 2. Upar wali consolidated list ko Products table ke sath Join karein 
taaki har sale ke sath product ka Name aur Category bhi dikhaye.
*/
-- Step: Dono sales tables ko pehle UNION se jora (Subquery) 
-- Phir usay Products table ke sath JOIN kiya
--select * from Online_Sales
SELECT 
    AllSales.SalesID,
    AllSales.Customer,
    AllSales.SaleDate,
    AllSales.Qty,
    p.SupplierName,    -- Products table se liya
    p.Category,       -- Products table se liya
    p.Price,
    (AllSales.Qty * p.Price) AS TotalRevenue -- Bonus: Calculation
FROM (
    -- Vertical Consolidation (UNION ALL)
    SELECT SalesID, ProdID, Customer, SaleDate, Qty FROM Online_Sales
    UNION ALL
    SELECT SaleID, ProdID, Customer, SaleDate, Qty FROM Store_Sales
) AS AllSales
INNER JOIN Products p ON AllSales.ProdID = p.ProdID
ORDER BY AllSales.SaleDate DESC;
