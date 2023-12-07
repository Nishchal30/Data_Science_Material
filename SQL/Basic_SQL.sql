-- Query to show all the databases
show databases;

-- Query to create a database
create database Sales;

-- Query to drop database
drop database Sales;

-- Query to use created database first to create table inside that database
use Sales;

-- Query to create a new table 
create table customer_info(
id int,
first_name varchar(25),
last_name varchar(25)
);

-- Query to show created tables
show tables;

-- insert data into created table
insert into customer_info values (1, "abc", "xyz");
-- OR
insert into customer_info (id, first_name, last_name) values (1, "abc", "xyz");

-- Query to fetch the values from the table based on specific conditions
select * from customer_info;
select * from customer_info where last_name  = "xyz";
select * from customer_info where last_name  = "xyz" or last_name = "gsj";
select * from customer_info where first_name = "abc" and last_name = "xyz";

-- Query to add multiple records in the table
insert into customer_info values (1, "abc", "xyz"), (2, "pre","gsj"),(3,"jhdh","djh");

-- Query to drop the table
drop table customer_info;

-- Create a table with a constraint of auto_increament
create table customer_info(
id int auto_increment,
first_name varchar(25),
last_name varchar(25),
primary key (id) -- primary key should be a column in which all the records are unique & not null and it has to be unique identifier of the table
);

-- to show the description of the table
describe customer_info;
-- OR
desc customer_info;

-- insert records in the new created table with constriants
insert into customer_info values (5, "abc","xyz"); -- for the first if the table has not start value for auto_increment then we need to specify start value at the time of inserting records.
-- If start value of auto_increment column is not specified it will by default take 1.

-- after that we need to just specify the column names and values directly
insert into customer_info (first_name, last_name) values ("abc","xyz"); -- Now we don't need to specify the id value

-- Constraints
-- 1) Not NULL
Alter table customer_info Modify column first_name varchar(25) not null; -- This will modify the already created table with new constriants to the column.

-- 2) UNIQUE
-- By default primary key is also unique, but the main difference between primary key and Unique constraint is:
-- we can assign Unique constriant to multiple columns, but this cannot be done with primary key.
-- In Unique constraint we can have null values but not in primary key.

create table customer_info(
id int auto_increment,
pan_number int unique, -- multiple 
house_number int unique, -- multiple
first_name varchar(25),
last_name varchar(25),
salary int not null,
primary key (id) 
);

-- Query to add UNIQUE constraint to single column in already created table
Alter table customer_info 
add unique (pan_number);

-- Query to add UNIQUE constraint to 2 combined columns in already created table
Alter table customer_info 
add constraint customername_pan unique (first_name, pan_number); -- customerid_pan is a constraint name which will combine id & pan and make that column UNIQUE.

desc customer_info;

insert into customer_info (pan_number, house_number, first_name, last_name, salary) values (1,2, "abc", "xyz", 2000), (1,5, "abc", "xyz", 2000);

select * from customer_info;

-- Drop the constraint 
alter table customer_info
drop index house_number;

create table customer_info(
id int,
pan_number int,
house_number int,
first_name varchar(25),
last_name varchar(25),
salary int not null,
primary key (id) 
);

-- Drop primary key constraint
alter table customer_info
drop primary key;
