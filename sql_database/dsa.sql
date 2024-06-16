show databases;
-- Q1:
use classicmodels;
show tables;
select *
from customers;
describe customers;
show index
from customers;
-- Q2: explain
desc customers;
select *
from customers
limit 10;
explain
select *
from customers
limit 10;
-- even we choose limit 10 type is still all
create index idx_phone on customers(phone);
explain
select *
from customers
where phone = "4155551450";
show global status like 'Innodb_buffer_pool_read_requests';