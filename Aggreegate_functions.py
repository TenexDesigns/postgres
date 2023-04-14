PostgreSQL provides a variety of aggregate functions that can be used to summarize and analyze data in a table.
Here are some of the most commonly used aggregate functions in PostgreSQL, along with code samples demonstrating their usage:

COUNT(): This function returns the number of rows in a table that match a certain condition.
SELECT COUNT(*) FROM my_table;



SUM(): This function returns the sum of a numeric column in a table that matches a certain condition.
SELECT SUM(price) FROM sales WHERE year = 2022;


AVG(): This function returns the average value of a numeric column in a table that matches a certain condition.
SELECT AVG(price) FROM sales WHERE year = 2022;


MIN(): This function returns the minimum value of a column in a table that matches a certain condition.
SELECT MIN(price) FROM sales WHERE year = 2022;


MAX(): This function returns the maximum value of a column in a table that matches a certain condition.
SELECT MAX(price) FROM sales WHERE year = 2022;


GROUP BY: This clause is used to group the result set by one or more columns.
SELECT year, SUM(price) FROM sales GROUP BY year;


HAVING: This clause is used to filter the result set based on aggregate values.
SELECT year, SUM(price) FROM sales GROUP BY year HAVING SUM(price) > 1000000;

DISTINCT: This clause is used to return only unique values from a column in a table.
SELECT DISTINCT year FROM sales;

These are just a few examples of the many aggregate functions and clauses available in PostgreSQL. 
For a complete list of aggregate functions and clauses, you can refer to the PostgreSQL documentation.



AGGREGATE FUNCTIONS ON JSON OBJECTS
**************************************************************************************

In PostgreSQL, aggregate functions can also be applied to JSON objects to extract summary statistics and other information.
Here are some of the aggregate functions commonly used with JSON objects:

json_agg(): This function aggregates multiple JSON objects into a single JSON array.
Example:
SELECT json_agg(my_json_column) FROM my_table;


json_object_agg(): This function aggregates multiple JSON key-value pairs into a single JSON object.
Example:
SELECT json_object_agg(key, value) FROM my_table;


jsonb_array_length(): This function returns the length of a JSON array.
Example:
SELECT jsonb_array_length(my_json_column) FROM my_table;


jsonb_object_keys(): This function returns the keys of a JSON object as a set.
Example:
SELECT jsonb_object_keys(my_json_column) FROM my_table;


jsonb_typeof(): This function returns the data type of a JSON object.
Example:
SELECT jsonb_typeof(my_json_column) FROM my_table;



In addition to the above functions, aggregate functions like mode(), stddev(), variance(), etc. can also be applied to JSON objects to extract summary statistics. 
However, its important to note that the usage of such functions on JSON objects can be complex and may require advanced knowledge 
of PostgreSQLs JSON functions and operators.

For example, to calculate the mode of a JSON array, you would first need to use jsonb_array_elements() to convert the array into individual elements,
and then use mode() on the resulting set:


SELECT mode(value) WITHIN GROUP (ORDER BY value)
FROM jsonb_array_elements(my_json_column->'my_array_key');
Similarly, to calculate the standard deviation of a JSON array, you would first need to use jsonb_array_elements()
to convert the array into individual elements, and then use stddev() on the resulting set:

SELECT stddev(value)
FROM jsonb_array_elements(my_json_column->'my_array_key');
Overall, while aggregate functions can be applied to JSON objects in PostgreSQL, 
their usage may require some additional knowledge and care, especially when dealing with complex JSON structures.






HERE IS MORE EXPLANATION
***********************************************************************


In this answer, I will provide an overview of some advanced aggregate functions in PostgreSQL and illustrate their usage with code samples.

Aggregate Functions in PostgreSQL
Aggregate functions in PostgreSQL are used to perform calculations on a set of rows and return a 
single row as a result postgresqltutorial.com. Some common aggregate functions include AVG(), COUNT(), MIN(), MAX(), and SUM() postgresqltutorial.com.

Advanced Aggregate Functions
STRING_AGG(): The STRING_AGG() function concatenates a list of strings and places a separator between them postgresqltutorial.com.

Syntax:

STRING_AGG (expression, separator [order_by_clause])
Example:

SELECT category, STRING_AGG(film_title, ', ' ORDER BY film_title)
FROM films
GROUP BY category;
In this example, the STRING_AGG() function concatenates film titles in each category,
separated by a comma and a space, and sorts the film titles alphabetically.

ARRAY_AGG(): The ARRAY_AGG() function accepts a set of values and returns an array in which each value in 
  the set is assigned to an element of the array postgresqltutorial.com.

Syntax:

ARRAY_AGG(expression [ORDER BY [sort_expression {ASC | DESC}], [...]])
Example:

SELECT category, ARRAY_AGG(film_title ORDER BY film_title)
FROM films
GROUP BY category;
In this example, the ARRAY_AGG() function creates an array of film titles for each category, sorted alphabetically.

Ordering within aggregate functions: PostgreSQL allows you to control the ordering of 
  input values within aggregate functions by using an ORDER BY clause postgresql.org.

Example:

SELECT category, STRING_AGG(film_title, ', ' ORDER BY film_release_date DESC)
FROM films
GROUP BY category;
In this example, the STRING_AGG() function concatenates film titles in each category, separated by a comma and a space,
and sorts the film titles by their release date in descending order.

Considerations
Aggregate functions return a null value when no rows are selected, except for COUNT() postgresql.org.
You can use the COALESCE() function to substitute zero or an empty array for null when necessary postgresql.org.

The performance of the COUNT() aggregate function may be slower when applied to the entire table in PostgreSQL, 
as it requires effort proportional to the size of the table postgresql.org.

In summary, PostgreSQL provides advanced aggregate functions like STRING_AGG() and ARRAY_AGG() to perform complex calculations on sets of rows.
Additionally, you can control the ordering of input values within aggregate functions using the ORDER BY clause.









































































































...
