CREATE VIEW product_sales(SKU, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
AS
SELECT a.SKU, a.order_no, a.qty, (a.qty*d.price) AS total_price, EXTRACT(YEAR FROM b.date) AS year, EXTRACT(MONTH FROM b.date) AS month, EXTRACT(DAY FROM b.date) AS day, EXTRACT(DOW FROM b.date) AS day_of_the_week
FROM contains a
JOIN orders b ON a.order_no = b.order_no
JOIN pay c ON a.order_no = c.order_no
JOIN product d ON a.SKU = d.SKU
JOIN customer e ON b.cust_no = e.cust_no