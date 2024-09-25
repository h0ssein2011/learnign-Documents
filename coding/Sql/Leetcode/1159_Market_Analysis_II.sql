use Leetcodes;
-- DROP TABLE IF EXISTS users;
-- CREATE TABLE users (
--     user_id INT,
--     join_date DATE,
--     favorite_brand VARCHAR(20)
-- );

-- INSERT INTO users (user_id, join_date, favorite_brand) VALUES
-- (1, '2019-01-01', 'Lenovo'),
-- (2, '2019-02-09', 'Samsung'),
-- (3, '2019-01-19', 'LG'),
-- (4, '2019-05-21', 'HP');

-- DROP TABLE IF EXISTS orders;
-- CREATE TABLE orders (
--     order_id INT,
--     order_date DATE,
--     item_id INT,
--     buyer_id INT,
--     seller_id INT
-- );

-- INSERT INTO orders (order_id, order_date, item_id, buyer_id, seller_id) VALUES
-- (1, '2019-08-01', 4, 1, 2),
-- (2, '2019-08-02', 2, 1, 3),
-- (3, '2019-08-03', 3, 2, 3),
-- (4, '2019-08-04', 1, 4, 2),
-- (5, '2019-08-04', 1, 3, 4),
-- (6, '2019-08-05', 2, 2, 4);

-- DROP TABLE IF EXISTS items;
-- CREATE TABLE items (
--     item_id INT,
--     item_brand VARCHAR(20)
-- );

-- INSERT INTO items (item_id, item_brand) VALUES
-- (1, 'Samsung'),
-- (2, 'Lenovo'),
-- (3, 'LG'),
-- (4, 'HP');

with  sorted_sells as 
(select * 
from
    (select o.*,i.item_brand, u.favorite_brand,RANK() over(partition by seller_id order by order_date) as rank_sell
from orders o 
join items i on o.item_id = i.item_id
join users u on u.user_id = o.seller_id

) T
where T.rank_sell = 2 and T.favorite_brand = T.item_brand
),no_seller as 
(select user_id 
from users where user_id not in (select distinct seller_id
from sorted_sells)

)
select seller_id ,'yes' as '2nd_item_fav_brand'   
from sorted_sells
UNION ALL
select * , 'no' as '2nd_item_fav_brand' 
from no_seller
order by seller_id
