-- 1. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- 2. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM superstore;

-- 3. Highest Sales Category
SELECT Category,
SUM(Sales) AS TotalSales
FROM superstore
GROUP BY Category
ORDER BY TotalSales DESC;

-- 4. Top 10 Customers
SELECT Customer_Name,
SUM(Sales) AS TotalSales
FROM superstore
GROUP BY Customer_Name
ORDER BY TotalSales DESC
LIMIT 10;

-- 5. Most Profitable State
SELECT State,
SUM(Profit) AS Profit
FROM superstore
GROUP BY State
ORDER BY Profit DESC;

-- 6. Monthly Sales
SELECT
MONTH(Order_Date) AS Month,
SUM(Sales) AS Sales
FROM superstore
GROUP BY Month;

-- 7. Loss-Making Products
SELECT Product_Name,
SUM(Profit) AS Profit
FROM superstore
GROUP BY Product_Name
HAVING Profit < 0
ORDER BY Profit;

-- 8. Region-wise Sales
SELECT Region,
SUM(Sales) AS Sales
FROM superstore
GROUP BY Region;
