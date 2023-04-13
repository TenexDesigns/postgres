

create table products(
  
  product_no integer,
  name text,
  price numeric CHECK(price > 0)
  discounted_price numeric CHECK (discounted_price > 0),
  check (price > discounted_price)
)



we can also combine the last check with the secnd last check by using the and logical operaltor


create table products(
  
  product_no integer,
  name text,
  price numeric CHECK(price > 0)
  discounted_price numeric CHECK (discounted_price > 0 and price > discounted_price )

)




WE CAN ALSO GIBE OUR CHECKS NAMES,Here we give the check that checks wherther the discount price is lower than the actual price ,a name of check_discount,
We can later interact with this name incase we want to alter the check later 



create table products(
  
  product_no integer,
  name text,
  price numeric CHECK(price > 0)
  discounted_price numeric CHECK (discounted_price > 0 and price > discounted_price ),
  CONSTRAINT check_discount CHECK check (price > discounted_price)
)










  THE CHECK CONSTRAINET
____________________________________________________________________________________________________________________________---

The check constraint is used to limit what values can be put in a column.
It is used to limit what values can be placed inside a column.
In this example it can be used to ensure that the values put in the hourly_pay are above 10.00


CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  hourly_pay DECIMAL (5,2),
  hire_date DATE,                                                 // We use this constarint to ensure that all values in the hourly_pay are above 10.00
  CONSTRAINT check_hourly_Pay CHECK (hourly_pay >= 10.00)        // This is the check constatint. We have given it a name of check_hourly_pay 
                                                                    ,so that we can easily identfy this constrainet

)


TO ADD A CHECK CONSTARINT TO A TABLE THAT ALREADY EXISTS.

---------> ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.00);



TO DELETE A CHECK, YOU DO SO IN THE FOLLOWING MANNER
You pass in the name you gave to your check

-------> ALTER TABLE employees DROP CHECK check_houlr_pay;




HERE ARE SOME MORE EXPLANATION
*********************************************************************************************************************************************

In PostgreSQL, a check constraint is a type of constraint that allows you to specify a Boolean expression that must be true for each row in a table. 
The Boolean expression can reference one or more columns in the table, and it can be as simple or as complex as needed.

Heres an example of a check constraint in PostgreSQL:




CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  salary NUMERIC(10, 2) NOT NULL,
  CONSTRAINT check_salary CHECK (salary > 0)
);



In this example, the employees table has a check constraint on the salary column. 
The check constraint specifies that the salary value must be greater than zero for each row in the table.
If any row violates this constraint, the INSERT or UPDATE operation will fail.

Check constraints have several uses in PostgreSQL:



Data validation: Check constraints can be used to validate the data being inserted or updated in a table.
  For example, you could use a check constraint to ensure that a date value is within a certain range, or that a string value matches a certain pattern.

Business logic enforcement: Check constraints can also be used to enforce business rules and logic.
  For example, you could use a check constraint to ensure that a discount percentage is not greater than 50%, or that a product quantity is not negative.

Performance optimization: Check constraints can be used to optimize query performance by limiting the amount of data that needs to be scanned.
  For example, you could use a check constraint to limit a query to only the rows that match a certain condition,
  which can improve query performance.






Overall, check constraints are a powerful feature of PostgreSQL that allow you to enforce
data integrity and ensure that your database conforms to your business rules and logic.














































































...
