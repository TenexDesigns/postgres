In PostgreSQL, the WHERE clause is used to filter rows from a table based on one or more conditions.
The WHERE clause is usually followed by a comparison operator, which is used to compare the values of two expressions.
Here are the most commonly used comparison operators in PostgreSQL:


1.Equal to: =

SELECT * FROM customers WHERE age = 25;

2.Not equal to: <> or !=

  SELECT * FROM customers WHERE age <> 25;
  SELECT * FROM customers WHERE age != 25;

3.Greater than: >
  
  SELECT * FROM customers WHERE age > 25;

4.Less than: <
  
  SELECT * FROM customers WHERE age < 25;

5.Greater than or equal to: >=
  
  SELECT * FROM customers WHERE age >= 25;

6.Less than or equal to: <=
  
  SELECT * FROM customers WHERE age <= 25;

7.Like: LIKE
  
  SELECT * FROM customers WHERE name LIKE 'J%';




The LIKE operator is used to match patterns in string data. 
The % wildcard character is used to match any number of characters, while the _ wildcard character is used to match a single character.

In addition to these basic operators, PostgreSQL also supports logical operators such as AND, OR, and NOT,
which can be used to combine multiple conditions in a WHERE clause. 
It also supports other comparison operators such as IN, BETWEEN, and IS NULL, which can be used for more complex filtering conditions.


































































































...
