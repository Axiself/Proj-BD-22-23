-- Query 1
SELECT DISTINCT customer.cust_name
FROM customer NATURAL JOIN parcel NATURAL JOIN has NATURAL JOIN product
WHERE parcel.order_date > '2022-12-31' AND parcel.order_date < '2024-01-01' AND product.price > 50;

-- Query 2
SELECT DISTINCT employee.emp_name
FROM parcel NATURAL JOIN process NATURAL JOIN employee NATURAL JOIN works NATURAL JOIN warehouse
WHERE parcel.order_date > '2022-12-31' AND parcel.order_date < '2023-02-01' AND warehouse.work_add NOT IN (
    SELECT work_add FROM office
);

-- Query 3
SELECT DISTINCT a.prod_name
FROM (
    SELECT product.sku, product.prod_name, SUM(has.qty) AS total_qty
    FROM sale NATURAL JOIN has NATURAL JOIN product
    GROUP BY product.prod_name
) AS a
WHERE total_qty >= ALL (
    SELECT b.total_qty
    FROM (
        SELECT SUM(has.qty) AS total_qty
        FROM sale NATURAL JOIN has NATURAL JOIN product
        GROUP BY product.sku
    ) AS b
);

-- Query 4
SELECT DISTINCT a.order_no, SUM(total_price)
FROM(
     SELECT DISTINCT order_no, price*qty AS total_price
     FROM sale NATURAL JOIN has NATURAL JOIN product
) AS a
GROUP BY a.order_no
ORDER BY a.order_no;