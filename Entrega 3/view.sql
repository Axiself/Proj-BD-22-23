CREATE VIEW product_sales(SKU, order_no, qty, total_price, year, month, day_of_month, day_of_week, city)
AS
SELECT b.SKU, b.order_no, b.qty, (b.qty*a.price), EXTRACT(YEAR FROM a.date), EXTRACT(MONTH FROM a.date), EXTRACT(DAY FROM a.date), EXTRACT(DOW FROM a.date), city
FROM(
    SELECT order_no, SKU, qty
    FROM contains
    WHERE order_no IN (SELECT order_no FROM pay)
) AS b NATURAL JOIN orders NATURAL JOIN customer NATURAL JOIN product AS a;