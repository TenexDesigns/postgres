In PostgreSQL, an alias is a temporary name given to a table or column.
It is used to make the table or column name more meaningful and understandable.
Aliases can be used in SELECT, FROM, and JOIN statements.

Here are some examples of how to use aliases in PostgreSQL:


  
  Alias for a table:
**********************************************************************************************************************************
Here we give the table another name 


Lets say we have a table called "employees" with columns "id", "name", and "salary". We can create an alias "e" for the employees table as follows:


SELECT e.id, e.name, e.salary FROM employees AS e;



Alias for a column:
**********************************************************************************************************************************
Using the same "employees" table, we can create an alias "wage" for the "salary" column as follows:

SELECT name, salary AS wage FROM employees;


Column aliases can be used with ORDER BY and GROUP BY clauses, but not with WHERE or HAVING clauses.

The AS keyword is optional, so you can also write it like this:

SELECT column_name alias_name FROM table_name;




Alias for a subquery:
**********************************************************************************************************************************

Syntax:
  
  SELECT alias.column_name FROM (subquery) AS alias;

  
  
  Code Sample:

Assuming we have two tables "orders" and "order_details" with columns "id", "product_name", "quantity", and "price".
We can create a subquery to get the total revenue for each order, and then create an alias "revenue" for the calculated total:
  

SELECT o.id, (od.quantity * od.price) AS revenue
FROM orders AS o
INNER JOIN order_details AS od ON o.id = od.order_id
WHERE o.status = 'complete'
ORDER BY o.id;




In this example, we join the "orders" and "order_details" tables, calculate the revenue for each order, 
and then use an alias "revenue" to display the calculated value in the SELECT statement.







Example with spaces in column alias:

SELECT first_name || ' ' || last_name "full name" FROM customer;


Column aliases can be used with ORDER BY and GROUP BY clauses, but not with WHERE or HAVING clauses.



















































































...
