-- combine two columns and make primary key

create table person(
id int,
first_name varchar(25),
last_name varchar(25),
age int,
primary key(id)
);

describe person;

ALTER TABLE person
add constraint pk_person primary key(id, last_name);

-- example of above 2 columns combined primary key
insert into person value (1, "abc","xyz",2000),(2, "abc","xyz",3000); -- this will be allowed as if both id & last_name will same then it will be not allowed.
-- we are combining id & last_name together to make a primary key
insert into person value (3, "abc","xyz",2000),(3, "abc","xyz",3000); -- this will give error as both id & last_name are same for both records.

select * from person;

-- drop the created constraint
alter table person
drop primary key; 

-- 3) Foriegn Key

create table orders (
orderid int not null,
order_number int,
id int,
primary key(orderid),
foreign key (id) references person(id)
);

insert into person values (1, "abc", "xyz", 24), (2, "abc1", "xyz1", 25), (3, "abc2", "xyz2", 26), (4, "ab3", "xyz3", 27);
select * from person;

insert into orders values (21,41, 1), (22, 25, 2);
select * from orders;

-- Inner Join
select * from person as ps
inner join orders as os
on ps.id = os.id;

-- Left Join
select * from person as ps
LEFT join orders as os
on ps.id = os.id; -- left join will fetch all the records from left table along with the common rows from right table.

-- Right Join
select * from person as ps
Right join orders as os
on ps.id = os.id; -- Right join will fetch all the records from Right table along with the common rows from left table.

-- Outer Join
select * from person as ps
Right join orders as os
on ps.id = os.id 
union                   -- union will remove duplicates after joining & union all will keep duplicates.
select * from person as ps
Left join orders as os
on ps.id = os.id;


-- Order By
select * from person as ps
inner join orders as os
on ps.id = os.id
order by ps.age desc;


