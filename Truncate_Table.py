In PostgreSQL, the TRUNCATE TABLE statement is used to delete all rows from a table. 
Unlike the DELETE statement, which deletes rows one by one and logs each deletion in the transaction log,
TRUNCATE TABLE removes all rows in a single operation, which makes it faster and more efficient for large tables.

Truncates deletes the all the data in the rows but it does not delete the columns .

Here is the syntax for the TRUNCATE TABLE statement:

TRUNCATE TABLE table_name [CASCADE | RESTRICT];



table_name: the name of the table to be truncated.
CASCADE: this option deletes all rows from the table and all dependent tables. 
 For example, if there is a foreign key constraint on the table, CASCADE will delete the rows from the dependent tables as well.
RESTRICT: this option prevents the TRUNCATE TABLE statement from executing if there are any foreign key constraints on the table.







Code Sample:

Let's say we have a table called 
"customers" with columns "id", "name", "email", and "phone". We can use the TRUNCATE TABLE statement to delete all rows from the table:

TRUNCATE TABLE customers;



If we want to delete all rows from the table and all dependent tables, we can use the CASCADE option:

TRUNCATE TABLE customers CASCADE;


If there are any foreign key constraints on the table and we want to prevent the TRUNCATE TABLE statement from executing, we can use the RESTRICT option:


TRUNCATE TABLE customers RESTRICT;





Note that TRUNCATE TABLE is a DDL (Data Definition Language) statement and it cannot be rolled back.
Once the TRUNCATE TABLE statement is executed, all data in the table is lost permanently.
Therefore, it is important to use this statement with caution and only when you are certain that you want to delete all data from the table.






















































...
