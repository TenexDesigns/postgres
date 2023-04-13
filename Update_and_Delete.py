HOW TO UPDATE AND DELETE DATA FROM A TABLE
_______________________________________________________________________________________________________________________________________________________________
To update data in a table we use

---------> UPDATE employees SET hourly_pay =10.25 WHERE employee_id = 6;


TO UPDATE MULTIPLE SETS OF DATA ,JUST SEPARATE THE DATA WITH A COMMA

Here we update the information of one employees whose id is 6.We update his hire date and his hourly pay.

---------> UPDATE employees SET  hourly_pay = 10.56, hire_date = "2023-01-07" WHERE employee_id = 6;

TO SET A VALUE EQUAL TO NULL
We hust set it to null

----------> UPDATE employees SET hourly_pay = NULL WHERE employee_id = 6;


TO UPDATE THE VALUE FOR THE WHOLE COLUMN INTO ONE VALUE,WE EXCLUDE THE WHERE CLAUSE
This will set alll values in the hourly_pay column equal to 12.45

----------> UPDATE employees SET hourly_pay = 12.45 ;



TO DELETE A ROW FROM A TABLE
________________________________________________________________________________
 To delete a row from a table ,use a WHERE clause, because else it will delete all of your rows.


This will delete the row whose employeee id is  6

-------> DELETE FROM employees WHERE employee_id = 6

DO NOT DO THIS AS IT WILL DELETE ALL OF YOUR ROWS IN YOU TABLE

-------> DELETE FROM employees






HERE IS MORE EXPLANATION
_______________________________________________________________________________________________________________________________________


In PostgreSQL, you can use the UPDATE and DELETE commands to modify the data in an existing table.

UPDATE command:
The UPDATE command is used to modify the existing data in a table. 
You can use it to update one or more columns in one or more rows that meet certain conditions. The basic syntax for the UPDATE command is:



UPDATE table_name
SET column_name = new_value
WHERE condition;

Here, table_name is the name of the table you want to update, column_name is the name of the column you want to modify,
new_value is the new value you want to set for that column, and condition is the criteria that determine which rows will be updated.

For example, to update the age of all users named "John" to 30, you would use the following command:


UPDATE users
SET age = 30
WHERE name = 'John';


DELETE command:
The DELETE command is used to remove one or more rows from a table.
You can use it to remove all rows or only some rows that meet certain conditions. The basic syntax for the DELETE command is:


  DELETE FROM table_name
WHERE condition;



Here, table_name is the name of the table you want to delete from, and condition is the criteria that determine which rows will be deleted.

For example, to delete all users who are older than 50, you would use the following command:



DELETE FROM users
WHERE age > 50;

Note that the DELETE command removes data permanently from the table, so its important to use it with caution and make sure you have a backup of your data.

In summary, the UPDATE and DELETE commands are powerful tools for modifying the data in an existing table in PostgreSQL.
Always make sure to double-check your conditions and test your queries on a small subset of your data before running them on the entire table.

































































































...
