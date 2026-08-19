SELECT 
    "Country",
    SUM(CAST(REGEXP_REPLACE("Net Revenue", '[^0-9.]', '', 'g') AS NUMERIC)) AS Country_Net_Revenue,
    ROUND(AVG(CAST(REGEXP_REPLACE("Net Revenue", '[^0-9.]', '', 'g') AS NUMERIC)), 2) AS Average_Transaction_Value
FROM local_sales
GROUP BY "Country"
ORDER BY 2 DESC; -- Sorts by column 2 (Country_Net_Revenue) largest to smallest 