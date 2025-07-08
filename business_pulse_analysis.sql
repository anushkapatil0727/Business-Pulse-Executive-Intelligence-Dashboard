-- Total Sales by Region
SELECT c.region, SUM(o.total_value) AS total_sales
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region;

-- Category-Wise Monthly Sales
SELECT DATE_TRUNC('month', order_date) AS month, category, SUM(total_value) AS sales
FROM orders
GROUP BY month, category
ORDER BY month;

-- Top 10 Customers by Lifetime Value
SELECT o.customer_id, SUM(o.total_value) AS lifetime_value
FROM orders o
GROUP BY o.customer_id
ORDER BY lifetime_value DESC
LIMIT 10;
