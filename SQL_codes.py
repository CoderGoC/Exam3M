# USE AdventureWorks2022
# SELECT TABLE_SCHEMA, TABLE_NAME
# FROM INFORMATION_SCHEMA.TABLES
# WHERE TABLE_SCHEMA != 'dbo'
# AND TABLE_TYPE != 'VIEW'
# ORDER BY TABLE_SCHEMA, TABLE_NAME;



 
# CREATE TABLE ProductCategories (
#     ProductCategoryID INT PRIMARY KEY,
#     CategoryName VARCHAR(255)
# );

# INSERT INTO ProductCategories (ProductCategoryID, CategoryName)
# SELECT 
#     pc.ProductCategoryID, 
#     pc.Name AS CategoryName
# FROM 
#     Production.ProductCategory pc;




# CREATE TABLE ProductSubcategories (
#     ProductSubcategoryID INT PRIMARY KEY,
#     SubcategoryName VARCHAR(255),
#     ProductCategoryID INT,
#     FOREIGN KEY (ProductCategoryID) REFERENCES ProductCategories(ProductCategoryID)
# );

# INSERT INTO ProductSubcategories (ProductSubcategoryID, SubcategoryName, ProductCategoryID)
# SELECT 
#     psc.ProductSubcategoryID,
#     psc.Name AS SubcategoryName,
#     psc.ProductCategoryID
# FROM 
#     Production.ProductSubcategory psc;
















# CREATE TABLE SalesOrderAnalysis (
#     SalesOrderID INT,
#     OrderDay INT,
#     OrderMonth INT,
#     OrderYear INT,
#     OrderMonthName VARCHAR(50),
#     DueDay INT,
#     DueMonth INT,
#     DueYear INT,
#     DueMonthName VARCHAR(50),
#     ShipDay INT,
#     ShipMonth INT,
#     ShipYear INT,
#     ShipMonthName VARCHAR(50),
#     SalesOrderNumber VARCHAR(50),
#     PurchaseOrderNumber VARCHAR(50),
#     CustomerID INT,
#     SalesPersonID INT,
#     BillToAddressID INT,
#     ShipToAddressID INT,
#     ShipMethodName VARCHAR(100),
#     CardType VARCHAR(50),
#     CurrencyRateID INT,
#     SubTotal DECIMAL(18, 4),
#     TaxAmt DECIMAL(18, 4),
#     Freight DECIMAL(18, 4),
#     TotalDue DECIMAL(18, 4),
#     TerritoryName VARCHAR(100),
#     TerritoryGroup VARCHAR(100),
#     SalesReasonNames VARCHAR(MAX)
# );



# INSERT INTO SalesOrderAnalysis (
#     SalesOrderID,
#     OrderDay,
#     OrderMonth,
#     OrderYear,
#     OrderMonthName,
#     DueDay,
#     DueMonth,
#     DueYear,
#     DueMonthName,
#     ShipDay,
#     ShipMonth,
#     ShipYear,
#     ShipMonthName,
#     SalesOrderNumber,
#     PurchaseOrderNumber,
#     CustomerID,
#     SalesPersonID,
#     BillToAddressID,
#     ShipToAddressID,
#     ShipMethodName,
#     CardType,
#     CurrencyRateID,
#     SubTotal,
#     TaxAmt,
#     Freight,
#     TotalDue,
#     TerritoryName,
#     TerritoryGroup,
#     SalesReasonNames
# )
# SELECT 
#     soh.[SalesOrderID],

#     -- Extract day, month, year from OrderDate
#     DAY(soh.[OrderDate]) AS [OrderDay],
#     MONTH(soh.[OrderDate]) AS [OrderMonth],
#     YEAR(soh.[OrderDate]) AS [OrderYear],
#     DATENAME(MONTH, soh.[OrderDate]) AS [OrderMonthName],

#     -- Extract day, month, year from DueDate
#     DAY(soh.[DueDate]) AS [DueDay],
#     MONTH(soh.[DueDate]) AS [DueMonth],
#     YEAR(soh.[DueDate]) AS [DueYear],
#     DATENAME(MONTH, soh.[DueDate]) AS [DueMonthName],

#     -- Extract day, month, year from ShipDate
#     DAY(soh.[ShipDate]) AS [ShipDay],
#     MONTH(soh.[ShipDate]) AS [ShipMonth],
#     YEAR(soh.[ShipDate]) AS [ShipYear],
#     DATENAME(MONTH, soh.[ShipDate]) AS [ShipMonthName],

#     soh.[SalesOrderNumber],
#     soh.[PurchaseOrderNumber],
#     soh.[CustomerID],
#     soh.[SalesPersonID],
#     soh.[BillToAddressID],
#     soh.[ShipToAddressID],
#     sm.[Name] AS [ShipMethodName],
#     cc.[CardType],
#     soh.[CurrencyRateID],
#     soh.[SubTotal],
#     soh.[TaxAmt],
#     soh.[Freight],
#     soh.[TotalDue],
#     st.[Name] AS [TerritoryName],
#     st.[Group] AS [TerritoryGroup],

#     -- Concatenate all sales reasons into one string
#     STRING_AGG(sr.[Name], ', ') AS SalesReasonNames
# FROM 
#     [AdventureWorks2022].[Sales].[SalesOrderHeader] AS soh
# LEFT JOIN 
#     [AdventureWorks2022].[Sales].[SalesTerritory] AS st
#     ON soh.[TerritoryID] = st.[TerritoryID]
# LEFT JOIN 
#     [AdventureWorks2022].[Purchasing].[ShipMethod] AS sm
#     ON soh.[ShipMethodID] = sm.[ShipMethodID]
# LEFT JOIN
#     [AdventureWorks2022].[Sales].[SalesOrderHeaderSalesReason] AS sohsr
#     ON soh.[SalesOrderID] = sohsr.[SalesOrderID]
# LEFT JOIN
#     [AdventureWorks2022].[Sales].[SalesReason] AS sr
#     ON sohsr.[SalesReasonID] = sr.[SalesReasonID]
# LEFT JOIN
#     [AdventureWorks2022].[Sales].[CreditCard] AS cc
#     ON soh.[CreditCardID] = cc.[CreditCardID]
# GROUP BY
#     soh.[SalesOrderID],
#     soh.[OrderDate],
#     soh.[DueDate],
#     soh.[ShipDate],
#     soh.[SalesOrderNumber],
#     soh.[PurchaseOrderNumber],
#     soh.[CustomerID],
#     soh.[SalesPersonID],
#     soh.[BillToAddressID],
#     soh.[ShipToAddressID],
#     sm.[Name],
#     cc.[CardType],
#     soh.[CurrencyRateID],
#     soh.[SubTotal],
#     soh.[TaxAmt],
#     soh.[Freight],
#     soh.[TotalDue],
#     st.[Name],
#     st.[Group];
