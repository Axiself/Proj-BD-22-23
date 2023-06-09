CREATE VIEW product_sales(SKU, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
AS
SELECT  a.SKU,
        a.order_no, a.qty,
        (a.qty*d.price),
        EXTRACT(YEAR FROM c.date),
        EXTRACT(MONTH FROM c.date),
        EXTRACT(DAY FROM c.date),
        EXTRACT(DOW FROM c.date),
        SUBSTRING(e.address FROM '(?!,)[^,]+$')
FROM contains a
JOIN pay b ON a.order_no = b.order_no
JOIN orders c ON a.order_no = c.order_no
JOIN product d ON a.SKU = d.SKU
JOIN customer e ON c.cust_no = e.cust_no;