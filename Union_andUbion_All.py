In PostgreSQL, UNION and UNION ALL are used to combine the result sets of two or more SELECT statements into a single result set.

UNION removes duplicate rows from the combined result set, while UNION ALL does not remove duplicates.

Here are examples of how to use UNION and UNION ALL in PostgreSQL:

                             UNION
Syntax:


  
  
  SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2;


Code Sample:

Lets say we have two tables "employees1" and "employees2" with the same columns "id", 
"name", and "salary". We can use UNION to combine the results of the two tables and remove any duplicate rows:

  
  SELECT id, name, salary
FROM employees1
UNION
SELECT id, name, salary
FROM employees2;





                             UNION ALL
Syntax:


  SELECT column1, column2, ...
FROM table1
UNION ALL
SELECT column1, column2, ...
FROM table2;




Code Sample:

Using the same tables "employees1" and "employees2", we can use UNION ALL to combine the results of the two tables and keep all duplicate rows:


  
  SELECT id, name, salary
FROM employees1
UNION ALL
SELECT id, name, salary
FROM employees2;



UNION and UNION ALL can also be used with more than two tables. In that case, we can chain multiple SELECT statements using UNION or UNION ALL:


SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2
UNION ALL
SELECT column1, column2, ...
FROM table3;





In this example, we first combine the results of "table1" and "table2" using UNION, and then combine the result with "table3" using UNION ALL.



























































































...
