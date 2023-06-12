-- OLAP 1

SELECT sku AS product, city, month, day_of_month, day_of_week, SUM(qty) AS total_amount, SUM(total_price) AS total_price
FROM product_sales
WHERE year = 2022
GROUP BY ROLLUP(sku,city,month,day_of_month,day_of_week);

--OLAP 2

SELECT month,day_of_week,AVG(total_price) AS valor_medio_diario
FROM product_sales
WHERE year = 2022
GROUP BY CUBE(month,day_of_week,total_price);