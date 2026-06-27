-- ============================================
-- sql server — class 3 homework
-- bikestores sample database
-- topics: group by · having · subqueries · exists
-- ============================================

-- q1: count how many products each brand has in the catalog.
-- show brand name and product count.
-- sort by count descending.

select count(product_name) as total_product,brand_name  from [production].[products] p 
inner join [production].[brands] b 
on b.brand_id=p.brand_id
group by brand_name
order by total_product desc

-- q2: for each category, show:
-- category name,
-- total number of products,
-- cheapest price,
-- most expensive price,
-- average price (rounded to 2 decimals).
-- sort by average price descending.

select 
c.category_name,
count(product_name) as total_product,
min(list_price) as min_price,
max(list_price) as max_prize,
avg(list_price) as avg_price
from [production].[products] p 
inner join [production].[categories]  c
on c.category_id=p.category_id
group by category_name
order by avg_price desc

-- q3: show the number of orders placed per order status.
-- display the status value and order count.
-- sort by order_status ascending.

select count (*) as order_summary,order_status
from [sales].[orders]
group by order_status
order by order_status asc

-- q4: for each store, calculate total revenue:
-- (quantity × list_price × (1 – discount)) from order_items.
-- show store name and total revenue.
-- sort by revenue descending.

select s.store_name,
sum(oi.quantity * oi.list_price * (1 - oi.discount)) as total_revenue
from [sales].[stores] s
inner join 
[sales].[orders] o
on s.store_id=o.store_id
inner join 
[sales].[order_items] oi
on o.order_id=oi.order_id
group by s.store_name
order by total_revenue desc

-- q5: show total number of products per brand per model year.
-- display brand name, model year, and product count.
-- sort by brand name then model year.

select count(*) total_product,b.brand_name,p.model_year from [production].[products] p
inner join [production].[brands] b 
on b.brand_id=p.brand_id
group by b.brand_name,p.model_year 
order by b.brand_name,p.model_year 

-- q6: find all brands that have more than 25 products in the catalog.
-- show brand name and product count.

select count(*) total_product,b.brand_name  from [production].[products] p
inner join [production].[brands] b 
on b.brand_id=p.brand_id
group by b.brand_name 
having count(*)>25
order by b.brand_name 

-- q7: among products from year 2018 only,
-- find categories whose average price is above $1500.
-- show category name, product count, and average price.

select c.category_name,count(*) as product_count ,avg(p.list_price) as avg_price,p.model_year from [production].[products] p
inner join [production].[categories] c
on p.category_id=c.category_id
where model_year=2018
group by c.category_name,p.model_year
having  avg(p.list_price)>1500

-- q8: find customers who have placed 3 or more orders.
-- show customer full name and order count.
-- sort by order count descending.

select c.first_name+ ' '+ c.last_name as full_name,count(o.order_id) order_count 
 from [sales].[orders] o
inner join [sales].[customers] c
on c.customer_id=o.customer_id
group by c.first_name,c.last_name
having count(o.order_id)>=3
order by order_count desc 
 
-- q9: find all products whose list price is higher than
-- the average list price of all products.
-- show product name and price.
-- sort by price descending.

select p.product_name,p.list_price from 
  [production].[products] p
  where list_price>(select avg(list_price) from production.products)
order by list_price desc

-- q10: find all orders placed by customers from state 'tx'.
-- use a subquery (not a join).
-- show order id, customer id, and order date.

select order_id,order_date,customer_id
from [sales].[orders]
where customer_id in (select customer_id from [sales].[customers]  
where state='tx')
 
-- q11: for each brand, show its average price,
-- but only for brands whose average price exceeds overall product average.
-- use a subquery in from (derived table).
-- show brand name and average price.

select 
    brand_name,avg_price
from
(select b.brand_name,avg(p.list_price) as avg_price from production.products p
inner join production.brands b
on b.brand_id = p.brand_id
group by b.brand_name
) as brand_avg
where avg_price >(select avg(list_price) from production.products);
 
-- q12: using exists:
-- find all customers who have placed at least one order.
-- show customer full name and email.

select c.first_name+ ' '+ c.last_name as full_name,c.email from [sales].[customers] c
where exists (select * from [sales].[orders] o
where c.customer_id=o.customer_id)

-- q13: using not exists:
-- find all products that have never appeared in any order (order_items).
-- show product name and list price.

select p.product_name,p.list_price from [production].[products] p
where not exists (select * from [sales].[order_items] oi
where oi.product_id=p.product_id)

 

