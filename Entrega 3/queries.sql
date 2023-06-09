--Query 1

WITH customer_total_price AS (
    SELECT c.cust_no, c.name, SUM(b.order_price) as total_price
    FROM(
        SELECT DISTINCT a.cust_no, SUM(product_price) as order_price
        FROM(
            SELECT DISTINCT cust_no, order_no, price*qty AS product_price
            FROM pay NATURAL JOIN contains NATURAL JOIN product
        ) AS a
        GROUP BY a.cust_no, a.order_no
    ) AS b NATURAL JOIN customer AS c
    GROUP BY c.cust_no
)

SELECT b.cust_no, b.name
FROM(
    SELECT MAX(customer_total_price.total_price) AS total_price
    FROM customer_total_price
) AS a NATURAL JOIN customer_total_price AS b;

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