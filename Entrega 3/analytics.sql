-- OLAP 1

SELECT sku AS product, city, month, day_of_the_month, day_of_the_week
FROM product_sales
WHERE year = 2022
GROUP BY CUBE(sku,city,month,day_of_the_month,day_of_the_week);

--OLAP 2

SELECT month,day_of_the_week,AVG(total_price) AS valor_medio_diario
FROM product_sales
WHERE year = 2022
GROUP BY CUBE(month,day_of_the_week,valor_medio_diario);