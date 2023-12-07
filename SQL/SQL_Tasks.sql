use ineuron;

create table if not exists SQL_TASKS (
ID INT,
Technology varchar(50)
);

INSERT INTO SQL_TASKS VALUES (1, "DS"), (1, "Tableau"),(1, "SQL"), (2,"R"), (2,"Power Bi"), (1, "Python");

SELECT * FROM SQL_TASKS;

-- Fetch all records with skills DS, Tableau, SQL, Python
SELECT * FROM SQL_TASKS WHERE Technology in ("DS", "Tableau", "SQL", "Python");

-- OR
SELECT DISTINCT(ID) FROM SQL_TASKS WHERE Technology = "DS" OR Technology = "Tableau" OR Technology = "SQL";

-- OR
SELECT ID FROM SQL_TASKS WHERE TECHNOLOGY = "DS" and ID in (
								SELECT ID FROM SQL_TASKS WHERE TECHNOLOGY = "Python" and ID in (
                                SELECT ID FROM SQL_TASKS WHERE TECHNOLOGY = "SQL"));
                                
                                
create table prod_info(
prod_id int,
prod_name varchar(30)
);

create table prod_likes(
user_id int,
prod_id int,
like_date date
);

insert into prod_info values (1001, "blog"), (1002, "Youtube"), (1003, "Education");
insert into prod_likes values (1, 1001, "2023-08-19"), (2, 1003, "2023-08-18");

select * from prod_info;
select * from prod_likes;

-- Query to return ID of products info that have 0 likes
select i.prod_id from prod_info as i 
left join prod_likes as l
on i.prod_id = l.prod_id
where like_date is null;
