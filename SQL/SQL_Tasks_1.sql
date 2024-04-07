USE INEURON;

CREATE TABLE IF not exists USA_Data (
ID INT,
NAME varchar(17),
COUNTRYCODE VARCHAR(3),
DISTRICT VARCHAR(20),
POPULATION INT);

SELECT * FROM USA_Data;

-- 1 Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
SELECT * FROM USA_data WHERE COUNTRYCODE = 'USA' and POPULATION > 100000;

-- 2  Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM USA_data WHERE COUNTRYCODE = 'USA' and POPULATION > 120000;

-- 3 Query all columns (attributes) for every row in the CITY table.
SELECT * FROM USA_data;

-- 4 Query all columns for a city in CITY with the ID 1661.
SELECT * FROM USA_data WHERE ID = 1661;

-- 5 Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM USA_data WHERE COUNTRYCODE = 'JPN';

-- 6  Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT NAME FROM USA_data WHERE COUNTRYCODE = 'JPN';


-- Query to find median of a column
with cte as
(select lat_n, 
row_number() over (order by lat_n desc) as row_num,
count(*) over () as total_rows
from station)

select round(lat_n, 4) from cte
where 
row_num = case
            when total_rows % 2 > 0 then (total_rows+1)/2
            when total_rows % 2 = 0 then ((total_rows/2) + (total_rows+1)/2)/2
          end
