CREATE VIEW product_sales(SKU, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
AS
SELECT  a.SKU,
        a.order_no, a.qty,
        (a.qty*d.price) AS total_price,
        EXTRACT(YEAR FROM c.date) AS year,
        EXTRACT(MONTH FROM c.date) AS month,
        EXTRACT(DAY FROM c.date) AS day,
        EXTRACT(DOW FROM c.date) AS day_of_the_week,
        SUBSTRING(e.address FROM '(?!,)[^,]+$') AS city
FROM contains a
JOIN pay b ON a.order_no = b.order_no
JOIN orders c ON a.order_no = c.order_no
JOIN product d ON a.SKU = d.SKU
JOIN customer e ON c.cust_no = e.cust_no