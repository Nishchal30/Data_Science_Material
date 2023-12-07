use ineuron;

-- Query to create a stored procedure
DELIMITER && -- used to end the statement
create procedure test ()
begin
select * from bank_details;
end &&

DELIMITER ; -- to change the end of statement again

call test(); -- call a created stored procedure

-- Query to create a stored procedure with input variable
DELIMITER && 
create procedure test1 (in marriage varchar(10))
begin
select * from bank_details where marital = marriage;
end &&

-- Query to drop a created stored procedure
DROP PROCEDURE ineuron.test1;
-- Query to call stored procedure with a input variable
call test1("single");

-- Query to create stored procedure with multiple outputs
DELIMITER && 
create procedure test2 (in marriage varchar(10))
begin
select * from bank_details where marital = marriage; -- 
select count(*) as total_count from bank_details; -- this will execute both the statements and will give both ouputs
end &&

call test2("single");

-- Query to create stored procedure with defining output variable
DELIMITER && 
create procedure test3 (out max_balance int)
begin
select max(balance) into max_balance from bank_details; -- specical query
end &&

call test3(@output); -- first need to store output in one variable with @
select @output; -- then fetch from that variable



