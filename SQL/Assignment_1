--Q1	List all brand names from the brands table.	Querying

 SELECT brand_name FROM [production].[brands];
 
--Q2	Show the product name and list price of all products, sorted from most expensive to cheapest.	Sorting

SELECT 
product_name,
list_price
FROM
[production].[products]
ORDER BY list_price DESC;
 
--Q3	Find all customers who live in the state of New York (NY).	Filtering

SELECT *
FROM [sales].[customers] 
WHERE state = 'NY';

--Q4	Show only the top 5 most expensive products in the store.	Querying

SELECT TOP 5 * 
FROM [production].[products]
ORDER BY list_price DESC;
 
--Q5	List all products with a price between $200 and $500, sorted by price ascending.	Filtering

SELECT * 
FROM [production].[products]
WHERE list_price BETWEEN 200 and 500
ORDER BY list_price ASC;
 
--Q6	Find all customers whose last name starts with the letter "S".	Filtering

SELECT *
FROM [sales].[customers]
WHERE last_name LIKE 's%'

--Q7	List all products that belong to category 6 (Mountain Bikes) OR category 7 (Road Bikes).	Filtering

SELECT 
* 
FROM [production].[products]
WHERE category_id = 6 OR category_id = 7;

Q8	Show all orders that have NOT been shipped yet (shipped_date is missing).	Filtering
Your answer:
SELECT *
FROM [sales].[orders]
WHERE [shipped_date] IS null;
 
--Q9	Display product name, brand ID, and a computed column showing 15% off the list price, labeled "Sale Price".	Querying

SELECT
	product_name,
	brand_id,
	list_price,
	list_price - ( list_price * 0.15 ) AS "Sale Price"
FROM [production].[products]
 
--Q10	Get a unique list of all cities where BikeStores customers live, sorted alphabetically.	Querying

 SELECT
           distinct city
FROM [sales].[customers]
ORDER BY city;

--Q11	List all staff members who are currently active (active = 1), showing their full name and email.	Filtering

SELECT
	first_name + '' + last_name as full_name, email
FROM [sales].[staffs]
WHERE active = 1
 
--Q12	Using UNION, get a combined list of all cities from both customers and stores (no duplicates), sorted A–Z.	Set Operators

SELECT city  
FROM [sales].[stores]
UNION
SELECT city 
FROM [sales].[customers]
ORDER BY city;
 
--Q13	Using EXCEPT, find product IDs that exist in order_items but are NOT in the products table.	Set Operators

SELECT product_id
FROM [sales].[order_items]
EXCEPT
SELECT product_id 
FROM [production].[products]

--Q14	List all products from the year 2016 with a price greater than $1,500, sorted by price descending.	Filtering

SELECT *
FROM [production].[products]
WHERE model_year >= 2016 AND list_price > 1500
ORDER BY list_price DESC;

--Q15	BONUS: Using UNION ALL, show Trek (brand_id = 9) products from 2016 and Surly (brand_id = 8) products from 2017. Include product name, brand, year, and price. Order by year then price descending.	Bonus

SELECT *
FROM [production].[products]
WHERE model_year >= 2016 AND brand_id = 9
UNION ALL
SELECT * 
FROM[production].[products]
WHERE model_year >= 2017 AND brand_id = 8
ORDER BY model_year, list_price DESC;
