--Query 1

SELECT d.cust_no, d.name, GREATEST(c.total_price)
FROM(
    SELECT b.cust_no, SUM(b.order_price) as total_price
    FROM(
        SELECT DISTINCT a.cust_no, SUM(product_price) as order_price
        FROM(
            SELECT DISTINCT cust_no, order_no, price*qty AS product_price
            FROM pay NATURAL JOIN contains NATURAL JOIN product
        ) AS a
        GROUP BY a.cust_no, a.order_no
    ) AS b
    GROUP BY b.cust_no
) as c NATURAL JOIN customer AS d;

--Query 2

SELECT DISTINCT employee.name
FROM employee NATURAL JOIN process NATURAL JOIN orders
WHERE EXTRACT(YEAR FROM orders.date) = 2022;

--Query 3

SELECT EXTRACT(MONTH FROM a.date) AS month, COUNT(*) AS no_of_orders
FROM(
    SELECT order_no, date
    FROM orders
    WHERE order_no NOT IN (SELECT order_no FROM pay) AND EXTRACT(YEAR FROM date) = 2022
) as a
GROUP BY EXTRACT(MONTH FROM a.date);