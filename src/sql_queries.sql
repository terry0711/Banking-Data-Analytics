-- Extracting recent transactions
SELECT * FROM Transactions WHERE Transaction_Timestamp >= '2024-01-01';

-- Finding top spending categories
SELECT Merchant_Category, AVG(Transaction_Amount) AS Avg_Spend
FROM Transactions
GROUP BY Merchant_Category
ORDER BY Avg_Spend DESC;

-- Detecting fraud hotspots
SELECT Location, COUNT(*) AS Fraud_Cases
FROM Transactions
WHERE Is_Fraud = 1
GROUP BY Location
ORDER BY Fraud_Cases DESC;

-- Identifying high-risk customers
SELECT Customer_ID, COUNT(*) AS Fraud_Count
FROM Transactions
WHERE Is_Fraud = 1
GROUP BY Customer_ID
HAVING COUNT(*) >= 3
ORDER BY Fraud_Count DESC;

-- Unusual Transactions Detection
SELECT * FROM Transactions
WHERE Transaction_Amount > 4000
AND Merchant_Category IN ('Dining', 'Grocery');
