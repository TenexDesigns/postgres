

In PostgreSQL, a data type specifies the type of data that can be stored in a column of a table.
PostgreSQL provides a wide range of built-in data types to support various kinds of data, 
including numbers, strings, dates and times, arrays, and more.

Here's an overview of some of the most commonly used data types in PostgreSQL:

INTEGER - stores a whole number, such as 1, 2, -5, etc.
BIGINT - stores a larger whole number than INTEGER, such as 123456789.
DECIMAL/NUMERIC - stores a fixed-precision decimal number, such as 3.1415 or 10.00. DECIMAL and NUMERIC are synonyms.
FLOAT/REAL - stores a floating-point number with a variable number of decimal places, such as 3.14 or 1.0E-10. REAL and FLOAT are synonyms.
TEXT - stores a variable-length string of characters, such as 'hello world'.
VARCHAR - stores a variable-length string of characters with a maximum length, such as VARCHAR(255).
DATE - stores a date value, such as '2023-04-13'.
TIME/TIMESTAMP - stores a time or date and time value, such as '23:59:59' or '2023-04-13 23:59:59'.
BOOLEAN - stores a true/false value.
ARRAY - stores an array of values of the same data type.
Character Types [ such as char, varchar, and text]
Numeric Types [ such as integer and floating-point number]
Temporal Types [ such as date, time, timestamp, and interval]
UUID [ for storing UUID (Universally Unique Identifiers) ]
Array [ for storing array strings, numbers, etc.]
JSON [ stores JSON data]
hstore [ stores key-value pair]
Special Types [ such as network address and geometric data]

Special data types:
In addition to the primitive data types, PostgreSQL also supports some special dat
a types that are related to network or geometric. These special data types are listed below: 

box: It is used to store rectangular box.
point: It is used to store geometric pair of numbers.
lseg: It is used to store line segment.
point: It is used to store geometric pair of numbers.
polygon:It is used to store closed geometric.
inet: It is used to store an IP4 address.
macaddr: It is used to store MAC address.

  
  Temporal data type:
This data type is used to store date-time data. PostgreSQL has 5 temporal data type: 

DATE is used to store the dates only.
TIME is used to stores the time of day values.
TIMESTAMP is used to stores both date and time values.
TIMESTAMPTZ is used to store a timezone-aware timestamp data type.
INTERVAL is used to store periods of time.


Overview of PostgreSQL data types
PostgreSQL supports the following data types:

Boolean
Character types such as char, varchar, and text.
Numeric types such as integer and floating-point number.
Temporal types such as date, time, timestamp, and interval
UUID for storing Universally Unique Identifiers
Array for storing array strings, numbers, etc.
JSON stores JSON data
hstore stores key-value pair
Special types such as network address and geometric data.

Boolean
A Boolean data type can hold one of three possible values: true, false or null. You use boolean or bool keyword to declare a column with the Boolean data type.

When you insert data into a Boolean column, PostgreSQL converts it to a Boolean value

1, yes, y, t, true values are converted to true
0, no, false, f values are converted to false.
When you select data from a Boolean column, PostgreSQL converts the values back e.g., t to true, f to false and space to null.

Character
PostgreSQL provides three character data types: CHAR(n), VARCHAR(n), and TEXT

CHAR(n) is the fixed-length character with space padded. 
If you insert a string that is shorter than the length of the column,
PostgreSQL pads spaces. If you insert a string that is longer than the length of the column, PostgreSQL will issue an error.
 VARCHAR(n) is the variable-length character string.  With VARCHAR(n),
  you can store up to n characters. PostgreSQL does not pad spaces when the stored string is shorter than the length of the column.
 TEXT is the variable-length character string. Theoretically, text data is a character string with unlimited length.

Numeric

PostgreSQL provides two distinct types of numbers:

integers
floating-point numbers
Integer
There are three kinds of integers in PostgreSQL:

Small integer ( SMALLINT) is 2-byte signed integer that has a range from -32,768 to 32,767.
Integer ( INT) is a 4-byte integer that has a range from -2,147,483,648 to 2,147,483,647.
Serial is the same as integer except that PostgreSQL will automatically generate and populate values into the SERIAL column.
This is similar to AUTO_INCREMENT column in MySQL or AUTOINCREMENT column in SQLite.
Floating-point number
There three main types of floating-point numbers:

float(n)  is a floating-point number whose precision, at least, n, up to a maximum of 8 bytes.
realor float8is a 4-byte floating-point number.
numeric or numeric(p,s) is a real number with p digits with s number after the decimal point. The numeric(p,s) is the exact number.
Temporal data types
The temporal data types allow you to store date and /or  time data. PostgreSQL has five main temporal data types:

DATEstores the dates only.

TIMEstores the time of day values.
TIMESTAMPstores both date and time values.
TIMESTAMPTZ is a timezone-aware timestamp data type. It is the abbreviation for timestamp with the time zone.
INTERVAL stores periods of time.
The TIMESTAMPTZ is the PostgreSQL’s extension to the SQL standard’s temporal data types.

Arrays
In PostgreSQL, you can store an array of strings, an array of integers, etc., in array columns.
The array comes in handy in some situations e.g., storing days of the week, months of the year.

JSON
PostgreSQL provides two JSON data types: JSON and JSONB for storing JSON data.

The JSON data type stores plain JSON data that requires reparsing for each processing, 
while JSONB data type stores JSON data in a binary format which is faster to process but slower to insert. 
In addition, JSONB supports indexing, which can be an advantage.

UUID
The UUID data type allows you to store Universal Unique Identifiers defined by RFC 4122 . 
The UUID values guarantee a better uniqueness than SERIAL and can be used to hide sensitive data exposed to the public such as values of id in URL.

Special data types
Besides the primitive data types, PostgreSQL also provides several special data types related to geometric and network.

box– a rectangular box.
line – a set of points.
point– a geometric pair of numbers.
lseg– a line segment.
polygon– a closed geometric.
inet– an IP4 address.
macaddr– a MAC address.
In this tutorial, we have introduced you to the PostgreSQL data types so that you can use them to create tables in the next tutorial.

Was this tutorial helpful ? 













In addition to these data types, PostgreSQL also provides several other data types for more specialized purposes, such as UUID, JSON, and XML.

Its worth noting that PostgreSQL allows users to define their own custom data types as well,
using the CREATE TYPE command. This can be useful for defining complex data structures or domain-specific data types.

Overall, PostgreSQL provides a wide range of data types to support various kinds of data, 
and you can choose the appropriate data type based on the type of data you need to store.



read more here 

https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/
https://www.geeksforgeeks.org/postgresql-data-types/
https://phoenixnap.com/kb/postgresql-data-types


















































...
